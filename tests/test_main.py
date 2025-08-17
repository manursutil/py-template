from unittest.mock import MagicMock, patch

from click.testing import CliRunner

from src.py_template.main import main


@patch("src.py_template.main.ProjectScaffolder")
@patch("src.py_template.main.Prompt")
@patch("src.py_template.main.Confirm")
def test_main_successful_scaffolding(
    mock_confirm: MagicMock,
    mock_prompt: MagicMock,
    mock_scaffolder: MagicMock,
):
    # Arrange
    runner = CliRunner()
    mock_scaffolder_instance = mock_scaffolder.return_value
    mock_scaffolder_instance.validate_project_name.return_value = True
    mock_scaffolder_instance.dev_dependencies = ["pytest", "ruff"]

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
    assert mock_scaffolder_instance.dependencies == ["requests", "fastapi"]
    assert mock_scaffolder_instance.dev_dependencies == ["pytest", "ruff"]
    assert mock_scaffolder_instance.include_docker is True
    mock_scaffolder_instance.scaffold_project.assert_called_once()


@patch("src.py_template.main.ProjectScaffolder")
@patch("src.py_template.main.Prompt")
def test_main_invalid_project_name(mock_prompt: MagicMock, mock_scaffolder: MagicMock):
    # Arrange
    runner = CliRunner()
    mock_scaffolder_instance = mock_scaffolder.return_value
    mock_scaffolder_instance.validate_project_name.side_effect = [False, True]

    # Simulate user inputs
    mock_prompt.ask.side_effect = [
        "invalid-name",
        "valid-project",
        "A test project",
        "Test Author",
    ]

    # Act
    result = runner.invoke(main, input="\n\n")

    # Assert
    assert result.exit_code == 0
    assert "Please try a different name." in result.output
    assert mock_scaffolder_instance.validate_project_name.call_count == 2
    assert mock_scaffolder_instance.project_name == "valid-project"


@patch("src.py_template.main.ProjectScaffolder")
def test_main_keyboard_interrupt(mock_scaffolder: MagicMock):
    # Arrange
    runner = CliRunner()
    mock_scaffolder_instance = mock_scaffolder.return_value
    mock_scaffolder_instance.scaffold_project.side_effect = KeyboardInterrupt

    # Act
    result = runner.invoke(main, input="test-project\ndescription\nauthor\n\n\n")

    # Assert
    assert result.exit_code == 0
    assert "Project creation interrupted by user." in result.output
