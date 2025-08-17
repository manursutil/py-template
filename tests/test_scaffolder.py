import os
import tempfile

import pytest

from src.py_template.scaffolder import ProjectScaffolder


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
