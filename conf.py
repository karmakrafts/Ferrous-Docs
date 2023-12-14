# @author Alexander Hinze
# @since 17/11/2023

import os
import sys
sys.path.append(os.path.relpath('_modules'))

# -- Project information -----------------------------------------------------

project = 'Ferrous'
copyright = '2023 Karma Krafts & associates'
author = 'Alexander Hinze'
version = '1.0'
release = 'nightly'
language = 'en'

# -- General configuration ---------------------------------------------------

extensions = [
	'sphinx.ext.autosectionlabel',
	'ferrous-highlighter'
]

autosectionlabel_prefix_document = True
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
highlight_language = 'Ferrous'

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_book_theme'
html_favicon = 'favicon.png'
html_logo = 'logo.png'
html_static_path = ['static']
html_css_files = ['_styles/ferrous_docs.css']
html_style = 'css/ferrous_docs.css'