# Development

## Setting Up Development Environment

1. Clone the repository:
```bash
git clone https://github.com/ndrezn/mkdocs-copy-markdown.git
cd mkdocs-copy-markdown
```

2. Install uv (if not already installed):
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or with pip
pip install uv
```

3. Sync dependencies and create virtual environment:
```bash
uv sync
```

This will automatically:
- Create a virtual environment
- Install the package in development mode
- Install all dependencies (including dev dependencies)

## Project Structure

```
mkdocs-copy-markdown/
├── mkdocs_copy_markdown/
│   ├── __init__.py
│   └── plugin.py
├── docs/
│   ├── index.md
│   ├── installation.md
│   ├── configuration.md
│   └── development.md
├── tests/
│   └── test_plugin.py
├── mkdocs.yml
├── pyproject.toml
├── setup.py
├── MANIFEST.in
├── .gitignore
└── README.md
```

## Plugin Architecture

The plugin uses MkDocs' event system to inject the copy functionality:

### Core Components

1. **Plugin Class**: `CopyMarkdownPlugin` extends `BasePlugin`
2. **Event Hook**: `on_page_content` modifies rendered HTML
3. **JavaScript**: Handles clipboard operations with fallbacks
4. **CSS**: Provides button styling

### Event Flow

1. MkDocs processes markdown → HTML
2. `on_page_content` is called with the HTML
3. Plugin injects button HTML, JavaScript, and CSS
4. Returns modified HTML to MkDocs

## Testing

### Manual Testing

Test the plugin with this documentation site:

```bash
uv run mkdocs serve
```

Visit `http://localhost:8000` and test the copy functionality.

### Unit Testing

Run the test suite:

```bash
uv run pytest tests/
```

### Testing with Different Themes

Test with different themes by temporarily adding them:

```bash
# Test with Material theme (already included)
uv run mkdocs serve

# Test with other themes
uv add mkdocs-rtd-dropdown --dev
uv run mkdocs serve -f test-configs/readthedocs.yml
```

## Code Style

The project follows standard Python conventions:

- PEP 8 for code style
- Type hints where appropriate
- Docstrings for public methods
- Clear variable and function names

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## Release Process

1. Update version in `pyproject.toml` and `__init__.py`
2. Update `CHANGELOG.md`
3. Create a git tag: `git tag v0.2.0`
4. Push tags: `git push --tags`
5. GitHub Actions will automatically:
   - Run tests across Python versions
   - Build the package
   - Publish to PyPI using trusted publishing

Manual build (for testing):
```bash
uv build
uv run twine check dist/*
```