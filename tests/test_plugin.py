import unittest
from unittest.mock import Mock, MagicMock
from mkdocs.structure.pages import Page
from mkdocs.structure.files import Files
from mkdocs.config.defaults import MkDocsConfig
from mkdocs_copy_markdown.plugin import CopyMarkdownPlugin


class TestCopyMarkdownPlugin(unittest.TestCase):
    
    def setUp(self):
        self.plugin = CopyMarkdownPlugin()
        self.plugin.config = {
            'button_text': 'Copy as Markdown',
            'button_position': 'top'
        }
        
    def test_plugin_initialization(self):
        """Test that plugin initializes correctly"""
        self.assertIsInstance(self.plugin, CopyMarkdownPlugin)
        self.assertEqual(self.plugin.config['button_text'], 'Copy as Markdown')
        self.assertEqual(self.plugin.config['button_position'], 'top')
    
    def test_on_page_content_with_markdown(self):
        """Test that button is added when page has markdown content"""
        # Mock objects
        page = Mock(spec=Page)
        page.markdown = "# Test Page\n\nThis is test content."
        config = Mock(spec=MkDocsConfig)
        files = Mock(spec=Files)
        
        html = "<h1>Test Page</h1><p>This is test content.</p>"
        
        result = self.plugin.on_page_content(html, page, config, files)
        
        # Check that button HTML is added
        self.assertIn('copy-markdown-container', result)
        self.assertIn('Copy as Markdown', result)
        self.assertIn('copyMarkdownToClipboard', result)
        self.assertIn('window.pageMarkdown', result)
        self.assertIn(page.markdown, result)
    
    def test_on_page_content_without_markdown(self):
        """Test that original HTML is returned when page has no markdown"""
        page = Mock(spec=Page)
        page.markdown = None
        config = Mock(spec=MkDocsConfig)
        files = Mock(spec=Files)
        
        html = "<h1>Test Page</h1>"
        
        result = self.plugin.on_page_content(html, page, config, files)
        
        # Should return original HTML unchanged
        self.assertEqual(result, html)
    
    def test_button_position_top(self):
        """Test button placement at top of content"""
        self.plugin.config['button_position'] = 'top'
        
        page = Mock(spec=Page)
        page.markdown = "Test content"
        config = Mock(spec=MkDocsConfig)
        files = Mock(spec=Files)
        
        html = "<p>Test content</p>"
        result = self.plugin.on_page_content(html, page, config, files)
        
        # Button should appear before the original HTML
        button_index = result.find('copy-markdown-container')
        content_index = result.find('<p>Test content</p>')
        self.assertLess(button_index, content_index)
    
    def test_button_position_bottom(self):
        """Test button placement at bottom of content"""
        self.plugin.config['button_position'] = 'bottom'
        
        page = Mock(spec=Page)
        page.markdown = "Test content"
        config = Mock(spec=MkDocsConfig)
        files = Mock(spec=Files)
        
        html = "<p>Test content</p>"
        result = self.plugin.on_page_content(html, page, config, files)
        
        # Button should appear after the original HTML
        button_index = result.find('copy-markdown-container')
        content_index = result.find('<p>Test content</p>')
        self.assertGreater(button_index, content_index)
    
    def test_custom_button_text(self):
        """Test custom button text configuration"""
        self.plugin.config['button_text'] = 'Custom Copy Text'
        
        page = Mock(spec=Page)
        page.markdown = "Test content"
        config = Mock(spec=MkDocsConfig)
        files = Mock(spec=Files)
        
        html = "<p>Test content</p>"
        result = self.plugin.on_page_content(html, page, config, files)
        
        self.assertIn('Custom Copy Text', result)
        self.assertNotIn('Copy as Markdown', result)
    
    def test_markdown_escaping(self):
        """Test that markdown content is properly escaped in JavaScript"""
        page = Mock(spec=Page)
        page.markdown = "Test with 'quotes' and \"double quotes\""
        config = Mock(spec=MkDocsConfig)
        files = Mock(spec=Files)
        
        html = "<p>Test content</p>"
        result = self.plugin.on_page_content(html, page, config, files)
        
        # Check that the markdown is properly represented in JavaScript
        self.assertIn('window.pageMarkdown', result)
        # The repr() function should properly escape quotes
        self.assertIn(repr(page.markdown), result)


if __name__ == '__main__':
    unittest.main()