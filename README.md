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
└── Dockerfile (optional)
```

## 🛠 Development

### Setup

```bash
git clone https://github.com/manursutil/py-template.git
cd py-template
uv sync
```

### Running Tests

```bash
uv run pytest
```

### Linting

```bash
uv run ruff check .
uv run ruff format .
```

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linting
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📋 Requirements

- Python 3.13+
- uv (will be installed automatically if not present)

## A Note from the Author

Py-Template started as a tool I built for **my own workflow** so it is a very opinionated way to spin up Python projects with the tools I use most frequently.

That said, I’d love to make it useful for a **broader audience**.
If you use a different stack, need extra integrations, or have ideas for improvement, please open an issue or PR.

Together we can make Py-Template a **universal scaffolding tool** for modern Python projects.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### 💡 Ideas & Feature Requests

We’d love to hear how Py-Template can better serve your workflow!
If you have suggestions, whether it’s for new templates (e.g., FastAPI, Flask, Data Science), CI/CD integrations (GitHub Actions, GitLab CI, etc.), or developer tools (MyPy, Black, Pre-commit, please open an issue or start a discussion.

Contributions of any size are welcome:

- 💬 Share ideas in issues/discussions
- 🔧 Submit pull requests for new features or improvements
- 🐞 Report bugs or unexpected behavior

Together we can make Py-Template a go-to tool for modern Python project scaffolding 🚀

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [uv](https://github.com/astral-sh/uv) for fast Python package management
- Uses [Rich](https://github.com/Textualize/rich) for beautiful terminal output
- Inspired by modern Python packaging practices
