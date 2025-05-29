# Installation & Configuration

## Requirements

- Python 3.7 or higher
- MkDocs 1.0.4 or higher

## Installation

### Install from PyPI

```bash
pip install mkdocs-copy-markdown
```

### Development Installation

For plugin development:

```bash
git clone https://github.com/ndrezn/mkdocs-copy-markdown.git
cd mkdocs-copy-markdown
uv sync
```

## Basic Configuration

Add the plugin to your `mkdocs.yml` configuration:

```yaml
plugins:
  - copy-markdown
```

That's it! The copy button will now appear on every page.

## Configuration Options

The plugin supports the following configuration options:

### `button_text`

- **Type**: `string`
- **Default**: `"Copy as Markdown"`
- **Description**: The text displayed on the copy button

```yaml
plugins:
  - copy-markdown:
      button_text: "Copy Source"
```

### `button_position`

- **Type**: `string`
- **Default**: `"top"`
- **Options**: `"top"` or `"bottom"`
- **Description**: Where to place the button relative to page content

```yaml
plugins:
  - copy-markdown:
      button_position: "bottom"
```

## Theme Compatibility

The plugin works with all MkDocs themes, including:

- **Material for MkDocs**
- **ReadTheDocs**
- **Bootstrap**
- **Cinder**
- **WindMill**
- Custom themes

The button styling is designed to integrate well with most theme color schemes.

## Advanced Usage

### Multiple Plugin Instances

You cannot configure multiple instances of the same plugin, but you can combine it with other plugins:

```yaml
plugins:
  - search
  - tags
  - copy-markdown
  - minify:
      minify_html: true
```

### Plugin Order

The copy-markdown plugin should generally be placed after content-modifying plugins but before minification plugins:

```yaml
plugins:
  - search
  - macros # Content modification
  - copy-markdown # Add copy button
  - minify # Minification (last)
```
