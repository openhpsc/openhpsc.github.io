# SPDX-License-Identifier: MIT
from datetime import datetime

project = "OpenHPSC"
author = "OpenHPSC contributors"
copyright = f"{datetime.now().year}, OpenHPSC contributors"
version = "0.2"
release = "0.2.2"

extensions = ["myst_parser", "sphinx.ext.mathjax", "sphinx.ext.autosectionlabel", "sphinx_copybutton"]
autosectionlabel_prefix_document = True
source_suffix = {".md": "markdown", ".rst": "restructuredtext"}
root_doc = "index"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
myst_enable_extensions = ["colon_fence", "deflist", "dollarmath", "fieldlist"]
myst_heading_anchors = 3
nitpicky = True
templates_path = ["_templates"]
html_theme = "sphinx_book_theme"
html_title = "OpenHPSC Documentation"
html_logo = "_static/openhpsc-logo.png"
html_favicon = "_static/openhpsc-logo.png"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_js_files = ["appearance.js"]
html_baseurl = "https://openhpsc.github.io/"
html_copy_source = False
html_show_sourcelink = False
html_theme_options = {
    "repository_url": "https://github.com/openhpsc/openhpsc.github.io",
    "repository_branch": "main",
    "path_to_docs": "docs",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "use_download_button": False,
    "show_navbar_depth": 2,
    "home_page_in_toc": True,
    "show_toc_level": 2,
    "navigation_with_keys": False,
    "logo": {"text": "Documentation"},
    "icon_links": [
        {"name": "Community discussions", "url": "https://github.com/openhpsc/community/discussions", "icon": "fa-solid fa-comments"},
        {"name": "Community issues", "url": "https://github.com/openhpsc/community/issues", "icon": "fa-solid fa-circle-exclamation"},
        {"name": "R&D project", "url": "https://github.com/orgs/openhpsc/projects/2", "icon": "fa-solid fa-table-columns"},
        {"name": "GitHub organization", "url": "https://github.com/openhpsc", "icon": "fa-brands fa-github"},
    ],
    "extra_footer": "Independent community initiative · Documentation v0.2",
}
html_context = {"default_mode": "light"}

# Hide a leading shell prompt in copied commands, preserving command flags.
copybutton_prompt_text = r"^\$ "
copybutton_prompt_is_regexp = True
copybutton_only_copy_prompt_lines = False
