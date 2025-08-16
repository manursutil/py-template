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
