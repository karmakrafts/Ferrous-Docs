# @author Alexander Hinze
# @since 17/11/2023

# -- Project information -----------------------------------------------------

project = 'Ferrous'
copyright = '2024 Karma Krafts & associates'
author = 'Alexander Hinze'
version = '1.2'
release = 'nightly'
language = 'en'

# -- General configuration ---------------------------------------------------

extensions = [
	'sphinx.ext.autosectionlabel',
	'sphinx-rtd-dark',
	'ferrous-pygments'
]

autosectionlabel_prefix_document = True
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
highlight_language = 'Ferrous'

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_favicon = 'favicon.png'
html_logo = 'logo.png'
html_static_path = ['_static']