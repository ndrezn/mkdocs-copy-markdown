from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page
from mkdocs.structure.files import Files
from mkdocs.config.defaults import MkDocsConfig


class CopyMarkdownPlugin(BasePlugin):
    config_scheme = (
        ("button_text", config_options.Type(str, default="Copy as Markdown")),
        ("button_position", config_options.Choice(["top", "bottom", "after-title"], default="after-title")),
    )

    def on_page_content(self, html, page: Page, config: MkDocsConfig, files: Files):
        if not page.markdown:
            return html

        button_text = self.config["button_text"]
        button_position = self.config["button_position"]

        copy_button_html = f"""<link rel="stylesheet" type="text/css" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/regular/style.css">
        
<div class="copy-markdown-container" style="margin: 10px 0;">
    <button id="copy-markdown-btn" class="copy-markdown-button" 
            onclick="copyMarkdownToClipboard()" 
            style="background: #007acc; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer; font-size: 14px; display: flex; align-items: center; gap: 6px;">
        <i id="copy-icon" class="ph ph-clipboard" style="font-size: 16px;"></i>
        <span>{button_text}</span>
    </button>
</div>
        
        <script>
        window.pageMarkdown = {repr(page.markdown)};
        let isAnimating = false;
        
        function copyMarkdownToClipboard() {{
            if (isAnimating) return;
            
            const icon = document.getElementById('copy-icon');
            
            if (navigator.clipboard && window.isSecureContext) {{
                navigator.clipboard.writeText(window.pageMarkdown).then(() => {{
                    showCopySuccess(icon);
                }}).catch(err => {{
                    console.error('Failed to copy: ', err);
                    fallbackCopyTextToClipboard(window.pageMarkdown);
                }});
            }} else {{
                fallbackCopyTextToClipboard(window.pageMarkdown);
            }}
        }}
        
        function showCopySuccess(icon) {{
            if (isAnimating) return;
            
            // If already showing success (checkmark), just reset the timer
            if (icon.className === 'ph ph-check') {{
                clearTimeout(window.copyTimeout);
                window.copyTimeout = setTimeout(() => {{
                    resetIcon(icon);
                }}, 2000);
                return;
            }}
            
            isAnimating = true;
            icon.style.opacity = '0';
            setTimeout(() => {{
                icon.className = 'ph ph-check';
                icon.style.opacity = '1';
                window.copyTimeout = setTimeout(() => {{
                    resetIcon(icon);
                }}, 1800);
            }}, 100);
        }}
        
        function showCopyError(icon) {{
            if (isAnimating) return;
            
            // If already showing error (X), just reset the timer
            if (icon.className === 'ph ph-x') {{
                clearTimeout(window.copyTimeout);
                window.copyTimeout = setTimeout(() => {{
                    resetIcon(icon);
                }}, 2000);
                return;
            }}
            
            isAnimating = true;
            icon.style.opacity = '0';
            setTimeout(() => {{
                icon.className = 'ph ph-x';
                icon.style.opacity = '1';
                window.copyTimeout = setTimeout(() => {{
                    resetIcon(icon);
                }}, 1800);
            }}, 100);
        }}
        
        function resetIcon(icon) {{
            icon.style.opacity = '0';
            setTimeout(() => {{
                icon.className = 'ph ph-clipboard';
                icon.style.opacity = '1';
                isAnimating = false;
            }}, 100);
        }}
        
        function fallbackCopyTextToClipboard(text) {{
            const textArea = document.createElement("textarea");
            textArea.value = text;
            textArea.style.top = "0";
            textArea.style.left = "0";
            textArea.style.position = "fixed";
            textArea.style.opacity = "0";
            
            document.body.appendChild(textArea);
            textArea.focus();
            textArea.select();
            
            const icon = document.getElementById('copy-icon');
            
            try {{
                const successful = document.execCommand('copy');
                if (successful) {{
                    showCopySuccess(icon);
                }} else {{
                    showCopyError(icon);
                }}
            }} catch (err) {{
                console.error('Fallback: Could not copy text: ', err);
                showCopyError(icon);
            }}
            
            document.body.removeChild(textArea);
        }}
        </script>
        
        <style>
        .copy-markdown-button:hover {{
            background: #005a9e !important;
        }}
        
        .copy-markdown-button:active {{
            transform: translateY(1px);
        }}
        
        #copy-icon {{
            transition: opacity 0.1s ease;
        }}
        </style>
        """

        if button_position == "top":
            return copy_button_html + html
        elif button_position == "bottom":
            return html + copy_button_html
        else:  # after-title
            import re
            # Find the first heading (h1, h2, h3, etc.)
            heading_pattern = r'(<h[1-6][^>]*>.*?</h[1-6]>)'
            match = re.search(heading_pattern, html, re.IGNORECASE | re.DOTALL)
            
            if match:
                # Insert button after the first heading
                heading_end = match.end()
                return html[:heading_end] + copy_button_html + html[heading_end:]
            else:
                # Fallback to top if no heading found
                return copy_button_html + html
