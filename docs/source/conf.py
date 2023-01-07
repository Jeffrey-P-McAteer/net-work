# Configuration file for the Sphinx documentation builder.

import os
import sys
# Add the folder with 'net_work/' in it to the import path
sys.path.insert(0, os.path.abspath(
  os.path.join(os.path.dirname(__file__), '..', '..')
))


# -- Project information

project = 'net-work'
copyright = '2022, Jeffrey McAteer <jeffrey@jmcateer.com>'
author = 'Jeffrey McAteer'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'



