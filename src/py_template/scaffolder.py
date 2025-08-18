import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from enum import Enum

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from .templates import (
    CI_YML_TEMPLATE,
    DOCKER_COMPOSE_TEMPLATE,
    DOCKERFILE_TEMPLATE,
    GITIGNORE_TEMPLATE,
    INIT_PY_TEMPLATE,
    MAIN_PY_TEMPLATE,
    MIT_LICENSE,
    README_TEMPLATE,
    TEST_MAIN_PY_TEMPLATE,
)

console = Console()


class ProjectType(str, Enum):
    CLI = "CLI Tool"
    WEB = "Web Application"
    LIB = "Python Library"
    DS = "Data Science"
    ML = "Machine Learning"
    BASIC = "Basic Package"


class ProjectScaffolder:
    def __init__(self):
        self.project_path: Path | None = None
        self.project_name: str = ""
        self.package_name: str = ""
        self.description: str = ""
        self.author: str = ""
        self.project_type: ProjectType = ProjectType.BASIC
        self.dependencies: list[str] = []
        self.dev_dependencies: list[str] = ["pytest", "ruff"]
        self.include_docker: bool = False
        self.include_github_actions: bool = False

    def validate_project_name(self, name: str) -> bool:
        if not name:
            return False

        if Path(name).exists():
            console.print(f"[red]Directory '{name}' already exists![/red]")
            return False

        if not re.match(r"^[a-z0-9_-]+$", name):
            console.print(
                "[red]Project name can only contain lowercase letters, numbers, hyphens, and underscores.[/red]"
            )
            return False

        return True

    def _directories_for_type(self) -> list[str]:
        base = [f"src/{self.package_name}", "tests", "docs"]

        if self.project_type == ProjectType.CLI:
            return base

        if self.project_type in (ProjectType.LIB, ProjectType.BASIC):
            return base

        if self.project_type == ProjectType.WEB:
            return base + [
                f"src/{self.package_name}/routers",
                f"src/{self.package_name}/models",
                f"src/{self.package_name}/core",
                "static",
                "templates",
            ]

        if self.project_type == ProjectType.DS:
            return base + [
                "notebooks",
                "data/raw",
                "data/processed",
                "reports",
                f"src/{self.package_name}/features",
                f"src/{self.package_name}/visualization",
            ]

        if self.project_type == ProjectType.ML:
            return base + [
                "notebooks",
                "data/raw",
                "data/processed",
                "models",
                "reports",
                f"src/{self.package_name}/features",
                f"src/{self.package_name}/training",
                f"src/{self.package_name}/inference",
            ]

        return base

    def create_project_structure(self):
        console.print(f"[green]Creating project structure for '{self.project_name}'...[/green]")

        self.project_path = Path(self.project_name)
        self.project_path.mkdir(exist_ok=True)

        os.chdir(self.project_path)

        directories = self._directories_for_type()

        for directory in directories:
            Path(directory).mkdir(parents=True, exist_ok=True)
            console.print(f"Created directory: {directory}")

    def initialize_uv_project(self):
        console.print("[blue]Initializing project with uv...[/blue]")

        try:
            subprocess.run(["uv", "init"], capture_output=True, text=True, check=True)
            console.print("uv project initialized successfully!")
        except subprocess.CalledProcessError as e:
            console.print(f"[red]Error initializing uv project: {e}[/red]")
            console.print("[red]Make sure uv is installed and available in PATH[/red]")
            sys.exit(1)
        except FileNotFoundError:
            console.print("[red]uv command not found. Please install uv first.[/red]")
            console.print(
                "[yellow]Install with: curl -LsSf https://astral.sh/uv/install.sh | sh[/yellow]"
            )
            sys.exit(1)

    def add_dependencies(self):
        if not self.dependencies:
            console.print("[yellow]No dependencies specified, skipping step...[/yellow]")
            return

        if self.dependencies:
            console.print(f"[blue]Adding dependencies: {', '.join(self.dependencies)}[/blue]")
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=console,
            ) as progress:
                for dep in self.dependencies:
                    task = progress.add_task(f"Installing {dep}...", total=None)

                    try:
                        subprocess.run(
                            ["uv", "add", dep.strip()],
                            capture_output=True,
                            text=True,
                            check=True,
                        )
                        progress.update(task, description=f"Installed {dep}")
                    except subprocess.CalledProcessError as e:
                        progress.update(task, description=f"Failed to install {dep}")
                        console.print(f"[red]Error adding dependency '{dep}': {e.stderr}[/red]")

        console.print(f"[blue]Adding dev dependencies: {', '.join(self.dev_dependencies)}[/blue]")
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            for dep in self.dev_dependencies:
                task = progress.add_task(f"Installing {dep}...", total=None)
                try:
                    subprocess.run(
                        ["uv", "add", "--dev", dep.strip()],
                        capture_output=True,
                        text=True,
                        check=True,
                    )
                    progress.update(task, description=f"Installed {dep}")
                except subprocess.CalledProcessError as e:
                    progress.update(task, description=f"Failed to install {dep}")
                    console.print(f"[red]Error adding dev dependency '{dep}': {e.stderr}[/red]")

    def create_license_file(self):
        console.print("[blue]Creating LICENSE file...[/blue]")

        license_content = MIT_LICENSE.format(year=datetime.now().year, author=self.author)

        with open("LICENSE", "w") as f:
            f.write(license_content)
        console.print("LICENSE file created")

    def create_readme(self):
        console.print("[blue]Creating README.md file...[/blue]")

        readme_content = README_TEMPLATE.format(
            project_name=self.project_name,
            description=self.description,
            package_name=self.package_name,
        )

        with open("README.md", "w") as f:
            f.write(readme_content)
        console.print("README.md file created")

    def create_source_files(self):
        console.print("[blue]Creating source files...[/blue]")

        init_content = INIT_PY_TEMPLATE.format(
            project_name=self.project_name,
            description=self.description,
        )
        init_path = Path(f"src/{self.package_name}/__init__.py")
        with open(init_path, "w") as f:
            f.write(init_content)
        console.print(f"Created {init_path}")

        main_content = MAIN_PY_TEMPLATE.format(
            project_name=self.project_name,
        )
        main_path = Path(f"src/{self.package_name}/main.py")
        with open(main_path, "w") as f:
            f.write(main_content)
        console.print(f"Created {main_path}")

    def create_test_files(self):
        console.print("[blue]Creating test files...[/blue]")

        tests_init_path = Path("tests/__init__.py")
        with open(tests_init_path, "w") as f:
            f.write("")
        console.print(f"Created {tests_init_path}")

        test_content = TEST_MAIN_PY_TEMPLATE.format(
            package_name=self.package_name,
        )
        test_path = Path("tests/test_main.py")
        with open(test_path, "w") as f:
            f.write(test_content)
        console.print(f"Created {test_path}")

    def create_gitignore(self):
        console.print("[blue]Creating .gitignore files...[/blue]")

        with open(".gitignore", "w") as f:
            f.write(GITIGNORE_TEMPLATE)
        console.print(".gitignore file created")

    def create_dockerfile(self):
        if not self.include_docker:
            return

        console.print("[blue]Creating Dockerfile...[/blue]")

        dockerfile_content = DOCKERFILE_TEMPLATE.format(
            package_name=self.package_name,
        )

        with open("Dockerfile", "w") as f:
            f.write(dockerfile_content)
        console.print("Dockerfile file created")

    def create_docker_compose(self):
        if not self.include_docker:
            return

        console.print("[blue]Creating docker-compose.yml...[/blue]")

        compose_content = DOCKER_COMPOSE_TEMPLATE.format(package_name=self.package_name)

        with open("docker-compose.yml", "w") as f:
            f.write(compose_content)
        console.print("docker-compose.yml created")

    def create_github_actions(self):
        if not self.include_github_actions:
            return

        console.print("[blue]Creating .github/workflows/ci.yml...[/blue]")

        ci_yml_content = CI_YML_TEMPLATE

        ci_yml_path = Path(".github/workflows/ci.yml")
        ci_yml_path.parent.mkdir(parents=True, exist_ok=True)

        with open(ci_yml_path, "w") as f:
            f.write(ci_yml_content)
        console.print(f"Created {ci_yml_path}")

    def scaffold_project(self):
        console.print(
            f"\n[bold green]🚀 Scaffolding Python project: {self.project_name}[/bold green]\n"
        )

        self.package_name = self.project_name.lower().replace("-", "_").replace(" ", "_")

        self.create_project_structure()
        self.initialize_uv_project()
        self.add_dependencies()

        self.create_license_file()
        self.create_readme()
        self.create_source_files()
        self.create_test_files()
        self.create_gitignore()
        self.create_dockerfile()
        self.create_docker_compose()
        self.create_github_actions()

        console.print(
            f"\n[bold green]✅ Project '{self.project_name}' scaffolded successfully![/bold green]"
        )
        console.print("\n[yellow]Next steps:[/yellow]")
        console.print(f"  1. cd {self.project_name}")
        console.print(f"  2. Start coding in src/{self.package_name}/main.py")
        console.print("  3. Run tests with: pytest")
        console.print("  4. Install in development mode: uv pip install -e .")

        if self.include_docker:
            console.print(f"  5. Build Docker image: docker build -t {self.project_name} .")
            console.print("  6. Run with Docker Compose: docker-compose up")
