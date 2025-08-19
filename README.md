# 🔥 UVForge

**Interactive Python project generator - like `create-react-app` but for Python**

Stop copying project structures and wrestling with configuration files. Answer a few questions, and get a perfectly structured Python project in seconds.

## ✨ Why UVForge?

**Before UVForge:**

```bash
mkdir my-project
cd my-project
touch setup.py pyproject.toml README.md requirements.txt .gitignore
mkdir src tests docs
# ... 15 more minutes of boilerplate setup
```

**With UVForge:**

```bash
uvforge
# Answer 4-5 quick questions
# ✅ Complete project ready in 30 seconds
```

### vs. cookiecutter

| Feature         | UVForge                      | cookiecutter                 |
| --------------- | ---------------------------- | ---------------------------- |
| Setup method    | Interactive Q&A              | Config files first           |
| Learning curve  | None - just answer questions | Need to understand JSON/YAML |
| Customization   | Guided prompts               | Pre-configure everything     |
| User experience | Like create-react-app        | Like filling out forms       |

## ✨ Features

- **Interactive CLI** - Guided setup with friendly prompts
- **Fast Setup** - Uses `uv` for fast project initialization
- **Modern Structure** - Creates `src` layout following Python packaging best practices
- **Testing Ready** - Includes `pytest` setup with example tests
- **Docker Support** - Optional Dockerfile generation
- **MIT License** - Automatically generates license file
- **Development Tools** - Pre-configured with `ruff` for linting

## 📦 Installation

### Using pip (Recommended)

```bash
pip install uvforge
```

## 🚀 Usage

Simply run the command and follow the interactive prompts:

```bash
uvforge
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
├── .github/
│   └── workflows/
│       └── ci.yml
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
git clone https://github.com/manursutil/uvforge.git
cd uvforge
uv sync

uv run pytest
uv run ruff check .
uv run ruff format .
```

## A Note from the Author

UVForge started as a tool I built for my own workflow so it is a very opinionated way to spin up Python projects with the tools I use most frequently.

That said, I'd love to make it useful for a broader audience. If you use a different stack, need extra integrations, or have ideas for improvement, please open an issue or PR.

Together we can make UVForge a universal scaffolding tool for modern Python projects 🚀

See [CONTRIBUTING.md](/docs/contributing.md) for guidelines on how to get involved.

## 🙏 Acknowledgments

- Built with [uv](https://github.com/astral-sh/uv) for fast Python package management
- Uses [Rich](https://github.com/Textualize/rich) for beautiful terminal output
- Inspired by modern Python packaging practices
