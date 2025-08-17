MIT_LICENSE = """MIT License

Copyright (c) {year} {author}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

README_TEMPLATE = """# {project_name}

{description}

## Installation

```bash
uv pip install -e .
```

## Usage

```python
from {package_name} import main

# Your code here
```

## Development

```bash
# Install development dependencies
uv pip install -e ".[dev]"

# Run tests
pytest

# Run linting
ruff check .
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
"""

DOCKERFILE_TEMPLATE = """FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install uv
RUN pip install uv

# Copy project files
COPY . .

# Install dependencies using uv sync
RUN uv sync --frozen

# Expose port (adjust as needed)
EXPOSE 8000

# Command to run the application
CMD ["uv", "run", "python", "-m", "{package_name}"]
"""

MAIN_PY_TEMPLATE = """def main():
    print("Hello from {project_name}!")


if __name__ == "__main__":
    main()
"""

INIT_PY_TEMPLATE = """\"\"\"{project_name} - {description}\"\"\"

__version__ = "0.1.0"
"""

TEST_MAIN_PY_TEMPLATE = """import pytest
from {package_name}.main import main


def test_main():
    # Add your tests here
    assert main() is None  # Placeholder test
"""

GITIGNORE_TEMPLATE = """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# Environments
.env
.venv
env/
venv/
"""

DOCKER_COMPOSE_TEMPLATE = """version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      - PYTHONPATH=/app
      - PYTHONDONTWRITEBYTECODE=1
      - PYTHONUNBUFFERED=1
    # Uncomment for development with live reload
    # command: uv run python -m {package_name}
    
  # Example: Add a database service
  # db:
  #   image: postgres:15
  #   environment:
  #     POSTGRES_DB: {package_name}
  #     POSTGRES_USER: user
  #     POSTGRES_PASSWORD: password
  #   ports:
  #     - "5432:5432"
  #   volumes:
  #     - postgres_data:/var/lib/postgresql/data

  # Example: Add Redis for caching
  # redis:
  #   image: redis:7-alpine
  #   ports:
  #     - "6379:6379"

# Uncomment if using database
# volumes:
#   postgres_data:
"""

CI_YML_TEMPLATE = """name: CI

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10", "3.11", "3.12", "3.13"]
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install uv
        uses: astral-sh/setup-uv@v3

      - name: Install dependencies
        run: uv sync

      - name: Lint with ruff
        run: uv run ruff check .

      - name: Test with pytest
        run: uv run pytest
"""
