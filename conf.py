# @author Alexander Hinze
# @since 17/11/2023

import os
import sys
sys.path.append(os.path.relpath('modules'))

# -- Project information -----------------------------------------------------

project = 'Ferrous'
copyright = '2023 Karma Krafts & associates'
author = 'Alexander Hinze'

# -- General configuration ---------------------------------------------------

extensions = [
	'sphinx.ext.autosectionlabel',
	'sphinx_rtd_dark_mode',
	'sphinx_new_tab_link',
	'ferrous-highlighter'
]

autosectionlabel_prefix_document = True
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_favicon = 'favicon.png'
html_static_path = ['static']