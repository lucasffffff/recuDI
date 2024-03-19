# añadimos los imports:
import os
import sys

sys.path.insert(0, os.path.abspath(''))
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Examen Lucas Feliu'
copyright = '2024, Lucas Feliu'
author = 'Lucas Feliu'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


# modificamos el archivo extensions añadiendo lo ssiguiente
extensions = [
    'sphinx.ext.autodoc',

    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
