# Contributing to UVForge

First off, thank you for considering contributing to **UVForge**! 🎉

It's people like you that make the open source community such a great place.

## Development Setup

1. Clone the repo:

```bash
git clone https://github.com/manursutil/py-template.git
cd py-template
```

2. Sync dependencies with uv:

```bash
uv sync
```

3. Run the tests:

```bash
uv run pytest
```

4. Run linting & formatting:

```bash
uv run ruff check .
uv run ruff format .
```

## How You Can Contribute

There are many ways to help improve UVForge:

- Share ideas — open an issue or start a discussion
- Report bugs — include steps to reproduce, expected vs. actual behavior
- Submit pull requests — fix bugs, add features, or improve docs
- Improve documentation — clarify usage or add examples

## Feature Requests

UVForge started as a tool for **my own workflow**, but I want to make it useful for a broader audience.

Ideas that would be especially valuable:

- New project templates
- CI/CD integrations (GitLab CI, etc.)
- Developer tools (MyPy, Pre-commit, Black, etc.)

If you'd like to propose one, please open an issue first so we can discuss it.

## Code Style

Use Ruff for linting and formatting:

```bash
uv run ruff check .
uv run ruff format .
```

Keep code type-annotated where possible.

Follow existing project structure and conventions.

## Pull Request Process

1. Fork the repository and create a feature branch:

```bash
git checkout -b feature/amazing-feature
```

2. Make your changes, run tests and linting.

3. Commit with a clear message:

```bash
git commit -m "Add amazing feature"
```

4. Push to your fork:

```bash
git push origin feature/amazing-feature
```

5. Open a Pull Request 🚀

Thank you for making UVForge better! 🙌
