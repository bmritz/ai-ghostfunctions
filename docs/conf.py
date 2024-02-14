"""Sphinx configuration."""

project = "AI Ghostfunctions"
author = "Brian M. Ritz"
copyright = "2023, Brian M. Ritz"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
