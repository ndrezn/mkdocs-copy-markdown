# MkDocs Copy Markdown

An MkDocs plugin that adds a "Copy as Markdown" button to every rendered documentation page, making it easy to copy content for pasting into AI assistants or sharing with others.

## Features

- **Easy Integration**: Simple plugin installation and configuration
- **Universal Compatibility**: Works with all MkDocs themes and configurations  
- **Cross-Browser Support**: Modern Clipboard API with fallback for legacy browsers
- **Customizable**: Configure button text and position
- **Visual Feedback**: Clear success/error indicators
- **Zero Dependencies**: No external JavaScript libraries required

## Quick Start

Install the plugin:

```bash
pip install mkdocs-copy-markdown
```

Add to your `mkdocs.yml`:

```yaml
plugins:
  - copy-markdown
```

That's it! The copy button will now appear on every page.

## Why Use This Plugin?

When working with documentation, users frequently need to copy markdown content to provide context to AI assistants like ChatGPT, Claude, or other LLMs. Rather than manually copying sections or trying to reconstruct markdown formatting, this plugin provides instant access to the original source with a single click.

Perfect for:
- **Providing context to AI assistants** with properly formatted documentation
- **Documentation teams** sharing content across projects
- **Open source projects** where users contribute documentation
- **Educational content** that students want to reference

## Live Demo

This documentation site itself uses the plugin! Look for the "Copy as Markdown" button at the top of this page to try it out.