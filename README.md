# AI Ghostfunctions

Write the docstring, call the function, get the results.

[![PyPI](https://img.shields.io/pypi/v/ai-ghostfunctions.svg)][pypi status]
[![Status](https://img.shields.io/pypi/status/ai-ghostfunctions.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/ai-ghostfunctions)][pypi status]
[![License](https://img.shields.io/pypi/l/ai-ghostfunctions)][license]

[![Read the documentation at https://ai-ghostfunctions.readthedocs.io/](https://img.shields.io/readthedocs/ai-ghostfunctions/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/bmritz/ai-ghostfunctions/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/bmritz/ai-ghostfunctions/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi status]: https://pypi.org/project/ai-ghostfunctions/
[read the docs]: https://ai-ghostfunctions.readthedocs.io/
[tests]: https://github.com/bmritz/ai-ghostfunctions/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/bmritz/ai-ghostfunctions
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Quickstart

```python
import os
from ai_ghostfunctions import ghostfunction

assert os.getenv("OPENAI_API_KEY")

@ghostfunction
def generate_random_words(n: int, startswith: str) -> list:
    """Return a list of `n` random words that start with `startswith`."""
    pass

generate_random_words(n=4, startswith="goo")
# ['gooze', 'goonie', 'gooble', 'goodum']

generate_random_words(n=2, startswith="foot")
# ['gooze', 'goonie', 'gooble', 'goodum']
```

By default, a ghostfunction will dispatch a sensible prompt to OpenAI GPT-4 that includes the function name, the docstring, and parameters.

## Customizations

You can control the prompt:

## Features

- TODO

## Requirements

- TODO

## Installation

You can install _AI Ghostfunctions_ via [pip] from [PyPI]:

```console
$ pip install ai-ghostfunctions
```

## Usage

Please see the [Command-line Reference] for details.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_AI Ghostfunctions_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/bmritz/ai-ghostfunctions/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/bmritz/ai-ghostfunctions/blob/main/LICENSE
[contributor guide]: https://github.com/bmritz/ai-ghostfunctions/blob/main/CONTRIBUTING.md
[command-line reference]: https://ai-ghostfunctions.readthedocs.io/en/latest/usage.html
