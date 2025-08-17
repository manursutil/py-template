# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Initial project scaffolding with `uv`
- Interactive CLI prompts
- `src` layout with `__init__.py` and `main.py`
- Example `pytest` setup
- Optional Dockerfile
- Pre-configured `ruff` for linting/formatting
- MIT License generation
- Automatic installation of `pytest` and `ruff` as dev dependencies
- "Next steps" guidance updated to include `ruff check .`
- Docker Compose support alongside Dockerfile generation
- Volume mounting in docker-compose.yml for development workflow
- Pre-configured examples for PostgreSQL and Redis services in docker-compose.yml
- Environment variables setup in Docker Compose (PYTHONPATH, PYTHONDONTWRITEBYTECODE, PYTHONUNBUFFERED)
- Github Actions CI support that generates `.github/workflows/ci.yml` file with uv, ruff, and pytest
- CI workflow template with Python 3.10-3.13 testing

### Changed

- Docker support prompt now mentions both Dockerfile and docker-compose.yml creation

### Fixed

- Correct spacing in file templates
