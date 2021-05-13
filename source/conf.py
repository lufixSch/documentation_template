"""
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from m2r import MdInclude
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Lukas GitHub'
copyright = '2021, Lukas Schüttler'
author = 'Lukas Schüttler'

language = 'en'

extensions = []
source_suffix = {}
exclude_patterns = []

favicon = ""
sidebars = {
    '**': [
        'about.html',
        'searchbox.html',
        'navigation.html',
        'localtoc.html',
    ],
}

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions.append('myst_parser')
source_suffix.update({
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
})

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_favicon = favicon
html_theme = 'alabaster'

# HTML theme configuration
html_theme_options = {
    'fixed_sidebar': True,
    'page_width': '90%',
    'sidebar_width': '20%',
    'body_max_width': '100%',

    'font_family':
        'system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", '
        'Arial, "Noto Sans", "Liberation Sans", sans-serif, '
        '"Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", '
        '"Noto Color Emoji"',

    'gray_1': 'var(--text-shade)',
    'gray_2': 'var(--background)',
    'gray_3': 'var(--background-shade)',

    'base_bg':  'var(--background)',
    'base_text':  'var(--text)',
    'hr_border':  'var(--border)',
    'body_bg':  'var(--background)',
    'body_text':  'var(--text-shade)',
    'footer_text':  'var(--text-shade)',
    'link':  'var(--text-primary)',
    'link_hover':  'var(--text-primary-shade)',
    'sidebar_text':  'var(--text-shade)',
    'sidebar_link_underscore':  'var(--text-shade)',
    'sidebar_search_button':  'var(--background-shade)',
    'sidebar_list':  'var(--text)',
    'anchor':  'var(--background-shade)',
    'anchor_hover_bg':  'var(--background-accent)',
    'table_border': 'var(--border)',

    'topic_bg': 'var(--background)',
    'code_highlight_bg': 'var(--background-shade)',
    'highlight_bg': 'var(--background-accent-shade)',
    'xref_border': 'var(--background)',
    'xref_bg': 'var(--background-shade)',
    'admonition_xref_border': 'var(--background-shade)',
    'admonition_xref_bg': 'var(--background)',
    'footnote_bg': 'var(--background-shade)',
    'footnote_border': 'var(--border)',
    'pre_bg': 'var(--background-accent-shade)',
    'narrow_sidebar_bg': 'var(--background)',
    'narrow_sidebar_fg': 'var(--background-shade)',
    'narrow_sidebar_link': 'var(--text-shade)',
    'viewcode_target_bg': 'var(--background-accent-shade)',
    'code_bg': 'var(--background-accent-shade)',
    'code_text': 'var(--code)',
    'code_hover': 'var(--text-shade)',
    'code_highlight': 'var(--text-primary-shade)'
}

html_sidebars = sidebars

html_domain_indices = True
html_use_index = True

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = [
    'css/colors.css',
    'css/code.css',
    'css/sidebar.css',
    'css/layout.css'
]


def setup(app):
    """
        Function to run on setup
    """
    # from m2r to make `mdinclude` work
    app.add_config_value('no_underscore_emphasis', False, 'env')
    app.add_config_value('m2r_parse_relative_links', False, 'env')
    app.add_config_value('m2r_anonymous_references', False, 'env')
    app.add_config_value('m2r_disable_inline_math', False, 'env')
    app.add_directive('mdinclude', MdInclude)
