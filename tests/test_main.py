from unittest.mock import MagicMock, patch

from click.testing import CliRunner

from src.uvforge.main import main
from src.uvforge.scaffolder import ProjectType


@patch("src.uvforge.main.ProjectScaffolder")
@patch("src.uvforge.main.Prompt")
@patch("src.uvforge.main.Confirm")
@patch("src.uvforge.main.inquirer")
def test_main_successful_scaffolding(
    mock_inquirer: MagicMock,
    mock_confirm: MagicMock,
    mock_prompt: MagicMock,
    mock_scaffolder: MagicMock,
):
    # Arrange
    runner = CliRunner()
    mock_scaffolder_instance = mock_scaffolder.return_value
    mock_scaffolder_instance.validate_project_name.return_value = True
    mock_scaffolder_instance.dev_dependencies = ["pytest", "ruff"]

    # Mock inquirer project type selection
    mock_inquirer.select.return_value.execute.return_value = "WEB"

    # Simulate user inputs
    mock_prompt.ask.side_effect = [
        "test-project",  # Project name
        "A test project",  # Description
        "Test Author",  # Author
        "requests, fastapi",  # Dependencies
    ]
    mock_confirm.ask.side_effect = [
        True,  # Add dependencies?
        False,  # Add more dependencies?
        True,  # Docker support?
        True,  # Github Actions support?
    ]

    # Act
    result = runner.invoke(main)

    # Assert
    assert result.exit_code == 0
    assert "Project Configuration:" in result.output

    # Verify that the scaffolder was called with the correct arguments
    mock_scaffolder_instance.validate_project_name.assert_called_once_with("test-project")
    assert mock_scaffolder_instance.project_name == "test-project"
    assert mock_scaffolder_instance.description == "A test project"
    assert mock_scaffolder_instance.author == "Test Author"
    assert mock_scaffolder_instance.project_type == ProjectType.WEB
    assert mock_scaffolder_instance.dependencies == ["requests", "fastapi"]
    assert mock_scaffolder_instance.dev_dependencies == ["pytest", "ruff"]
    assert mock_scaffolder_instance.include_docker is True
    mock_scaffolder_instance.scaffold_project.assert_called_once()


@patch("src.uvforge.main.ProjectScaffolder")
@patch("src.uvforge.main.Prompt")
@patch("src.uvforge.main.Confirm")
@patch("src.uvforge.main.inquirer")
def test_main_invalid_project_name(
    mock_inquirer: MagicMock,
    mock_confirm: MagicMock,
    mock_prompt: MagicMock,
    mock_scaffolder: MagicMock,
):
    # Arrange
    runner = CliRunner()
    mock_scaffolder_instance = mock_scaffolder.return_value
    mock_scaffolder_instance.validate_project_name.side_effect = [False, True]

    # Mock inquirer project type selection
    mock_inquirer.select.return_value.execute.return_value = "BASIC"

    # Simulate user inputs
    mock_prompt.ask.side_effect = [
        "invalid-name",
        "valid-project",
        "A test project",
        "Test Author",
    ]
    mock_confirm.ask.side_effect = [
        False,  # Add dependencies?
        True,  # Docker support?
        True,  # Github Actions support?
    ]

    # Act
    result = runner.invoke(main)

    # Assert
    assert result.exit_code == 0
    assert "Please try a different name." in result.output
    assert mock_scaffolder_instance.validate_project_name.call_count == 2
    assert mock_scaffolder_instance.project_name == "valid-project"
    assert mock_scaffolder_instance.project_type == ProjectType.BASIC
    assert mock_scaffolder_instance.include_docker is True
    assert mock_scaffolder_instance.include_github_actions is True
    mock_scaffolder_instance.scaffold_project.assert_called_once()


@patch("src.uvforge.main.ProjectScaffolder")
@patch("src.uvforge.main.Prompt")
@patch("src.uvforge.main.Confirm")
@patch("src.uvforge.main.inquirer")
def test_main_keyboard_interrupt(
    mock_inquirer: MagicMock,
    mock_confirm: MagicMock,
    mock_prompt: MagicMock,
    mock_scaffolder: MagicMock,
):
    # Arrange
    runner = CliRunner()
    mock_scaffolder_instance = mock_scaffolder.return_value
    mock_scaffolder_instance.scaffold_project.side_effect = KeyboardInterrupt

    # Mock inquirer project type selection
    mock_inquirer.select.return_value.execute.return_value = "CLI"

    # Simulate user inputs
    mock_prompt.ask.side_effect = ["test-project", "description", "author"]
    mock_confirm.ask.side_effect = [False, False, False]  # No for all confirms

    # Act
    result = runner.invoke(main)

    # Assert
    assert result.exit_code == 0
    assert "Project creation interrupted by user." in result.output


@patch("src.uvforge.main.ProjectScaffolder")
@patch("src.uvforge.main.Prompt")
@patch("src.uvforge.main.Confirm")
@patch("src.uvforge.main.inquirer")
def test_main_no_dependencies(
    mock_inquirer: MagicMock,
    mock_confirm: MagicMock,
    mock_prompt: MagicMock,
    mock_scaffolder: MagicMock,
):
    # Arrange
    runner = CliRunner()
    mock_scaffolder_instance = mock_scaffolder.return_value
    mock_scaffolder_instance.validate_project_name.return_value = True

    # Mock inquirer project type selection
    mock_inquirer.select.return_value.execute.return_value = "LIB"

    # Simulate user inputs
    mock_prompt.ask.side_effect = ["test-project", "desc", "author"]
    mock_confirm.ask.side_effect = [False, True, True]  # No dependencies, yes to docker and github

    # Act
    result = runner.invoke(main)

    # Assert
    assert result.exit_code == 0
    assert "Dependencies: None" in result.output
    assert mock_scaffolder_instance.dependencies == []
    assert mock_scaffolder_instance.include_docker is True
    assert mock_scaffolder_instance.include_github_actions is True
    mock_scaffolder_instance.scaffold_project.assert_called_once()


@patch("src.uvforge.main.ProjectScaffolder")
@patch("src.uvforge.main.Prompt")
@patch("src.uvforge.main.Confirm")
@patch("src.uvforge.main.inquirer")
def test_main_different_project_types(
    mock_inquirer: MagicMock,
    mock_confirm: MagicMock,
    mock_prompt: MagicMock,
    mock_scaffolder: MagicMock,
):
    """Test that different project types are properly set"""
    # Arrange
    runner = CliRunner()
    mock_scaffolder_instance = mock_scaffolder.return_value
    mock_scaffolder_instance.validate_project_name.return_value = True

    # Test Data Science project type
    mock_inquirer.select.return_value.execute.return_value = "DS"

    # Simulate user inputs
    mock_prompt.ask.side_effect = ["ds-project", "Data Science Project", "Data Scientist"]
    mock_confirm.ask.side_effect = [False, False, False]  # No for all confirms

    # Act
    result = runner.invoke(main)

    # Assert
    assert result.exit_code == 0
    assert mock_scaffolder_instance.project_type == ProjectType.DS
    assert mock_scaffolder_instance.project_name == "ds-project"
    assert mock_scaffolder_instance.description == "Data Science Project"
    assert mock_scaffolder_instance.author == "Data Scientist"
    mock_scaffolder_instance.scaffold_project.assert_called_once()


@patch("src.uvforge.main.ProjectScaffolder")
@patch("src.uvforge.main.Prompt")
@patch("src.uvforge.main.Confirm")
@patch("src.uvforge.main.inquirer")
def test_main_ml_project_type(
    mock_inquirer: MagicMock,
    mock_confirm: MagicMock,
    mock_prompt: MagicMock,
    mock_scaffolder: MagicMock,
):
    """Test Machine Learning project type selection"""
    # Arrange
    runner = CliRunner()
    mock_scaffolder_instance = mock_scaffolder.return_value
    mock_scaffolder_instance.validate_project_name.return_value = True

    # Test Machine Learning project type
    mock_inquirer.select.return_value.execute.return_value = "ML"

    # Simulate user inputs
    mock_prompt.ask.side_effect = ["ml-project", "ML Project", "ML Engineer"]
    mock_confirm.ask.side_effect = [False, False, False]  # No for all confirms

    # Act
    result = runner.invoke(main)

    # Assert
    assert result.exit_code == 0
    assert mock_scaffolder_instance.project_type == ProjectType.ML
    assert mock_scaffolder_instance.project_name == "ml-project"
    assert mock_scaffolder_instance.description == "ML Project"
    assert mock_scaffolder_instance.author == "ML Engineer"
    mock_scaffolder_instance.scaffold_project.assert_called_once()
