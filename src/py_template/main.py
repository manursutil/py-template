import click
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, Prompt

from .scaffolder import ProjectScaffolder

console = Console()


@click.command()
def main():
    console.print(
        Panel.fit(
            "[bold blue]🐍 Py-Template[/bold blue]\n\n"
            "Let's create your new Python project step by step!",
            border_style="blue",
        )
    )

    scaffolder = ProjectScaffolder()

    console.print("\n[bold cyan]Step 1: Project Information[/bold cyan]")
    while True:
        project_name = Prompt.ask("What's the name of your project?", default="my-python-project")
        if scaffolder.validate_project_name(project_name):
            break
        console.print("[yellow]Please try a different name.[/yellow]\n")

    scaffolder.project_name = project_name

    description = Prompt.ask(
        "Provide a brief description of your project", default="A Python project"
    )
    scaffolder.description = description

    author = Prompt.ask("What's your name? (for the license)", default="Your Name")
    scaffolder.author = author

    console.print("\n[bold cyan]Step 2: Dependencies[/bold cyan]")
    console.print(
        "[dim]You can add popular packages like: requests, fastapi, pandas, numpy, etc.\n"
        "(pytest and ruff are added for you as dev dependencies)[/dim]"
    )

    dependencies = []
    while True:
        add_deps = Confirm.ask("Do you want to add any dependencies?", default=False)
        if not add_deps:
            break

        dep_input = Prompt.ask(
            "Enter dependencies (comma-separated, e.g., 'requests, fastapi, pytest')", default=""
        )

        if dep_input.strip():
            new_deps = [dep.strip() for dep in dep_input.split(",") if dep.strip()]
            dependencies.extend(new_deps)
            console.print(f"[green]Added: {', '.join(new_deps)}[/green]")

        if dependencies:
            console.print(f"[blue]Current dependencies: {', '.join(dependencies)}[/blue]")

        if not Confirm.ask("Add more dependencies?", default=False):
            break

    scaffolder.dependencies = dependencies

    console.print("\n[bold cyan]Step 3: Additional Features[/bold cyan]")
    docker = Confirm.ask(
        "Would you like to include Docker support? (creates a Dockerfile + docker-compose.yml)",
        default=False,
    )
    scaffolder.include_docker = docker

    github_actions = Confirm.ask(
        "Would you like to include support for Github Actions CI?",
        default=True,
    )
    scaffolder.include_github_actions = github_actions

    console.print("\n[bold]Project Configuration:[/bold]")
    console.print(f"  📦 Project Name: [cyan]{scaffolder.project_name}[/cyan]")
    console.print(f"  📝 Description: [cyan]{scaffolder.description}[/cyan]")
    console.print(f"  👤 Author: [cyan]{scaffolder.author}[/cyan]")
    if scaffolder.dependencies:
        console.print(f"  📚 Dependencies: [cyan]{', '.join(scaffolder.dependencies)}[/cyan]")
    else:
        console.print("  📚 Dependencies: [dim]None[/dim]")

    console.print("  🛠️  Dev Dependencies: [cyan]pytest, ruff[/cyan]")
    console.print(f"  🐳 Docker: [cyan]{'Yes' if scaffolder.include_docker else 'No'}[/cyan]")
    console.print(
        f"  🚀 GitHub Actions: [cyan]{'Yes' if scaffolder.include_github_actions else 'No'}[/cyan]"
    )

    try:
        scaffolder.scaffold_project()
    except KeyboardInterrupt:
        console.print("\n[red]Project creation interrupted by user.[/red]")
    except Exception as e:
        console.print(f"\n[red]An error occurred: {e}[/red]")


@click.command()
def version():
    console.print("[blue]Py-Template v1.0.0[/blue]")


if __name__ == "__main__":
    main()
