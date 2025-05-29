# MkDocs Copy Markdown

An MkDocs plugin that adds a "Copy as Markdown" button to every rendered documentation page, making it easy to copy content for pasting into AI assistants or sharing with others.

## Features

- Adds a customizable "Copy as Markdown" button to every page
- Works with both modern browsers (using Clipboard API) and legacy browsers (fallback method)
- Configurable button text and position
- Visual feedback when copying succeeds or fails
- No external dependencies beyond MkDocs

## Installation

Install the plugin using pip:

```bash
pip install mkdocs-copy-markdown
```

Or install from source:

```bash
git clone https://github.com/ndrezn/mkdocs-copy-markdown.git
cd mkdocs-copy-markdown
pip install .
```

## Configuration

Add the plugin to your `mkdocs.yml` configuration file:

```yaml
plugins:
  - copy-markdown
```

### Options

You can customize the plugin behavior with these options:

```yaml
plugins:
  - copy-markdown:
      button_text: "Copy as Markdown"  # Text displayed on the button
      button_position: "top"           # Position: "top" or "bottom"
```

#### Configuration Options

- **button_text** (default: "Copy as Markdown"): The text displayed on the copy button
- **button_position** (default: "top"): Where to place the button relative to page content. Options are:
  - `"top"`: Places the button above the page content
  - `"bottom"`: Places the button below the page content

## Usage

Once installed and configured, the plugin will automatically add a copy button to every page in your MkDocs site. Users can click the button to copy the original markdown source of the page to their clipboard.

The button includes visual feedback:
- ✓ Copied! - Success message in green
- ✗ Copy failed - Error message in red

## Browser Compatibility

The plugin uses the modern Clipboard API when available and falls back to the legacy `document.execCommand('copy')` method for older browsers, ensuring broad compatibility.

## Development

To set up for development:

```bash
git clone https://github.com/ndrezn/mkdocs-copy-markdown.git
cd mkdocs-copy-markdown
pip install -e .
```

## License

This project is licensed under the MIT License.