# 🐍 Py-Template

**Py-Template brings the `create-react-app` experience to Python**, an interactive, zero-friction CLI that bootstraps projects with `uv`, testing, linting, and optional Docker support. It generates a modern, well-structured Python project with best practices baked in, so you can start coding right away.

## ✨ Features

- **Interactive CLI** - Guided setup with friendly prompts
- **Fast Setup** - Uses `uv` for fast project initialization
- **Modern Structure** - Creates `src` layout following Python packaging best practices
- **Testing Ready** - Includes `pytest` setup with example tests
- **Docker Support** - Optional Dockerfile generation
- **MIT License** - Automatically generates license file
- **Development Tools** - Pre-configured with `ruff` for linting

## 📦 Installation

### Using pipx (Recommended)

```bash
pipx install git+https://github.com/manursutil/py-template.git
```

### Using uv (Development)

```bash
git clone https://github.com/manursutil/py-template.git
cd py-template
uv pip install -e .
```

## 🚀 Usage

Simply run the command and follow the interactive prompts:

```bash
py-template
```

### Demo

![Demo](/docs/img/demo.gif)

### Generated Project Structure

```
my-awesome-app/
├── src/
│   └── my_awesome_app/
│       ├── __init__.py
│       └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── docs/
├── LICENSE
├── README.md
├── .gitignore
├── pyproject.toml
└── Dockerfile + docker-compose.yml (optional)
```

## Development

See [CONTRIBUTING.md](/docs/contributing.md) for full details on setting up a dev environment, running tests, and contributing.

Quick start:

```bash
git clone https://github.com/manursutil/py-template.git
cd py-template
uv sync

uv run pytest
uv run ruff check .
uv run ruff format .
```

## A Note from the Author

Py-Template started as a tool I built for my own workflow so it is a very opinionated way to spin up Python projects with the tools I use most frequently.

That said, I’d love to make it useful for a broader audience.If you use a different stack, need extra integrations, or have ideas for improvement, please open an issue or PR.

Together we can make Py-Template a universal scaffolding tool for modern Python projects 🚀

See [CONTRIBUTING.md](/docs/contributing.md) for guidelines on how to get involved.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [uv](https://github.com/astral-sh/uv) for fast Python package management
- Uses [Rich](https://github.com/Textualize/rich) for beautiful terminal output
- Inspired by modern Python packaging practices
