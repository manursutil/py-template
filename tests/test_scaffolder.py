import os
import tempfile

import pytest

from src.uvforge.scaffolder import ProjectScaffolder, ProjectType


@pytest.fixture
def scaffolder():
    return ProjectScaffolder()


def test_validate_project_name_valid(scaffolder: ProjectScaffolder):
    assert scaffolder.validate_project_name("my-project")
    assert scaffolder.validate_project_name("my_project")
    assert scaffolder.validate_project_name("myproject")


def test_validate_project_name_invalid(scaffolder: ProjectScaffolder):
    assert not scaffolder.validate_project_name("my project")
    assert not scaffolder.validate_project_name("my-project!")
    assert not scaffolder.validate_project_name("My-Project")


def test_scaffold_project_creates_project_directory():
    scaffolder = ProjectScaffolder()
    scaffolder.project_name = "test-project"
    scaffolder.description = "A test project"
    scaffolder.author = "Test Author"
    scaffolder.dependencies = ["requests"]
    scaffolder.dev_dependencies = ["pytest", "ruff"]
    scaffolder.include_docker = True
    scaffolder.include_github_actions = True

    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        scaffolder.scaffold_project()

        project_path = os.path.join(tmpdir, scaffolder.project_name)
        assert os.path.isdir(project_path)

        # Check for some expected files
        assert os.path.isfile(os.path.join(project_path, "pyproject.toml"))
        assert os.path.isfile(os.path.join(project_path, "README.md"))
        assert os.path.isfile(os.path.join(project_path, "Dockerfile"))
        assert os.path.isfile(os.path.join(project_path, ".github/workflows/ci.yml"))


def test_directories_for_type_basic(scaffolder: ProjectScaffolder):
    """Test that BASIC project type creates basic directories"""
    scaffolder.project_name = "test-project"
    scaffolder.package_name = "test_project"
    scaffolder.project_type = ProjectType.BASIC

    directories = scaffolder._directories_for_type()

    expected = ["src/test_project", "tests", "docs"]
    assert directories == expected


def test_directories_for_type_cli(scaffolder: ProjectScaffolder):
    """Test that CLI project type creates basic directories"""
    scaffolder.project_name = "test-project"
    scaffolder.package_name = "test_project"
    scaffolder.project_type = ProjectType.CLI

    directories = scaffolder._directories_for_type()

    expected = ["src/test_project", "tests", "docs"]
    assert directories == expected


def test_directories_for_type_lib(scaffolder: ProjectScaffolder):
    """Test that LIB project type creates basic directories"""
    scaffolder.project_name = "test-project"
    scaffolder.package_name = "test_project"
    scaffolder.project_type = ProjectType.LIB

    directories = scaffolder._directories_for_type()

    expected = ["src/test_project", "tests", "docs"]
    assert directories == expected


def test_directories_for_type_web(scaffolder: ProjectScaffolder):
    """Test that WEB project type creates web-specific directories"""
    scaffolder.project_name = "test-project"
    scaffolder.package_name = "test_project"
    scaffolder.project_type = ProjectType.WEB

    directories = scaffolder._directories_for_type()

    expected = [
        "src/test_project",
        "tests",
        "docs",
        "src/test_project/routers",
        "src/test_project/models",
        "src/test_project/core",
        "static",
        "templates",
    ]
    assert directories == expected


def test_directories_for_type_ds(scaffolder: ProjectScaffolder):
    """Test that DS project type creates data science directories"""
    scaffolder.project_name = "test-project"
    scaffolder.package_name = "test_project"
    scaffolder.project_type = ProjectType.DS

    directories = scaffolder._directories_for_type()

    expected = [
        "src/test_project",
        "tests",
        "docs",
        "notebooks",
        "data/raw",
        "data/processed",
        "reports",
        "src/test_project/features",
        "src/test_project/visualization",
    ]
    assert directories == expected


def test_directories_for_type_ml(scaffolder: ProjectScaffolder):
    """Test that ML project type creates machine learning directories"""
    scaffolder.project_name = "test-project"
    scaffolder.package_name = "test_project"
    scaffolder.project_type = ProjectType.ML

    directories = scaffolder._directories_for_type()

    expected = [
        "src/test_project",
        "tests",
        "docs",
        "notebooks",
        "data/raw",
        "data/processed",
        "models",
        "reports",
        "src/test_project/features",
        "src/test_project/training",
        "src/test_project/inference",
    ]
    assert directories == expected


def test_create_project_structure_with_different_types():
    """Test that create_project_structure creates correct directories for different project types"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Change to temp directory first
        os.chdir(tmpdir)

        # Test Web Application
        web_scaffolder = ProjectScaffolder()
        web_scaffolder.project_name = "web-project"
        web_scaffolder.package_name = "web_project"
        web_scaffolder.project_type = ProjectType.WEB

        web_scaffolder.create_project_structure()

        # Check that web-specific directories were created
        # Note: create_project_structure changes to the project directory
        assert os.path.isdir("src/web_project")
        assert os.path.isdir("tests")
        assert os.path.isdir("docs")
        assert os.path.isdir("src/web_project/routers")
        assert os.path.isdir("src/web_project/models")
        assert os.path.isdir("src/web_project/core")
        assert os.path.isdir("static")
        assert os.path.isdir("templates")

        # Go back to temp directory for next test
        os.chdir(tmpdir)

        # Test Data Science
        ds_scaffolder = ProjectScaffolder()
        ds_scaffolder.project_name = "ds-project"
        ds_scaffolder.package_name = "ds_project"
        ds_scaffolder.project_type = ProjectType.DS

        ds_scaffolder.create_project_structure()

        # Check that DS-specific directories were created
        # Note: create_project_structure changes to the project directory
        assert os.path.isdir("src/ds_project")
        assert os.path.isdir("tests")
        assert os.path.isdir("docs")
        assert os.path.isdir("notebooks")
        assert os.path.isdir("data/raw")
        assert os.path.isdir("data/processed")
        assert os.path.isdir("reports")
        assert os.path.isdir("src/ds_project/features")
        assert os.path.isdir("src/ds_project/visualization")


def test_project_type_enum_values():
    """Test that ProjectType enum has correct values"""
    from src.uvforge.scaffolder import ProjectType

    assert ProjectType.CLI == "CLI Tool"
    assert ProjectType.WEB == "Web Application"
    assert ProjectType.LIB == "Python Library"
    assert ProjectType.DS == "Data Science"
    assert ProjectType.ML == "Machine Learning"
    assert ProjectType.BASIC == "Basic Package"


def test_scaffolder_initialization():
    """Test that ProjectScaffolder initializes with correct default values"""
    scaffolder = ProjectScaffolder()

    assert scaffolder.project_path is None
    assert scaffolder.project_name == ""
    assert scaffolder.package_name == ""
    assert scaffolder.description == ""
    assert scaffolder.author == ""
    assert scaffolder.project_type == ProjectType.BASIC
    assert scaffolder.dependencies == []
    assert scaffolder.dev_dependencies == ["pytest", "ruff"]
    assert scaffolder.include_docker is False
    assert scaffolder.include_github_actions is False
