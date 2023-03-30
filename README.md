# AI Ghostfunctions

Write the docstring, call the function, get the results.

[![PyPI](https://img.shields.io/pypi/v/ai-ghostfunctions.svg)][pypi status]
[![Status](https://img.shields.io/pypi/status/ai-ghostfunctions.svg)][pypi status]

[![Tests](https://github.com/bmritz/ai-ghostfunctions/workflows/Tests/badge.svg)][tests]

[pypi status]: https://pypi.org/project/ai-ghostfunctions/
[read the docs]: https://ai-ghostfunctions.readthedocs.io/
[tests]: https://github.com/bmritz/ai-ghostfunctions/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/bmritz/ai-ghostfunctions
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Installation

You can install via [pip] from [PyPI]:

```console
$ pip install ai-ghostfunctions
```

## Quickstart

```python
import os
from ai_ghostfunctions import ghostfunction

assert os.getenv("OPENAI_API_KEY")

@ghostfunction
def sanitize_messy_string(messy_string: str) -> list[dict]:
    """Return a list of dicts that contain the data from `messy_string`."""
    pass

@ghostfunction
def generate_random_words(n: int, startswith: str) -> list:
    """Return a list of `n` random words that start with `startswith`."""
    pass

sanitize_messy_string(messy_string="""name|age|nickname
John Brighton Bradford,  34,  J.B
        Grace B., "24", Grace""")
# '[\n    {"name": "John Brighton Bradford", "age": 34, "nickname": "J.B"},\n    {"name": "Grace B.", "age": 24, "nickname": "Grace"}\n]'

generate_random_words(n=4, startswith="goo")
# "['gooze', 'goonie', 'gooble', 'goodum']"

generate_random_words(n=3, startswith="foot")
# "['football', 'footstep', 'footnote']"
```

By default, a ghostfunction will dispatch a sensible prompt to OpenAI GPT-4 that includes the function name, the docstring, and function arguments, parse the result from OpenAI and return it as the result of the function.

Ghostfunctions will retry and send the data to gpt-3.5-turbo if it looks like the OPENAI_API_KEY does not have access to gpt-4.

Yes, it returns strings for now. I'll update that probably soon, so expect a breaking change there.

## Customizations

You can control the prompt:

```python
import os
from ai_ghostfunctions import ghostfunction
from ai_ghostfunctions.keywords import SYSTEM, USER
from ai_ghostfunctions.types import Message

assert os.getenv("OPENAI_API_KEY")

@ghostfunction(prompt_function=lambda f, **kwargs: [
    Message(role=USER, content=f"tell me a slightly insulting joke about this function name: {f.__name__}.")
])
def recursive_function_that_will_recurse():
    """Recurse until you go crazy."""
    pass

recursive_function_that_will_recurse()
# 'Why did the programmer name his function "recursive_function_that_will_recurse"? Because he wanted to make absolutely sure that no one would confuse it for a function that actually does something useful.'
```

Heh. Not bad.

Prompts to gpt-4 and gpt-3.5-turbo are of type `List[ai_ghostfunctions.types.Message]`.

See [ghostfunctions.py](./src/ai_ghostfunctions/ghostfunctions.py#48) for the default prompt.

## Requirements

- [![Python Version](https://img.shields.io/pypi/pyversions/ai-ghostfunctions)][pypi status]
- openai Python client library

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [![License](https://img.shields.io/pypi/l/ai-ghostfunctions)][license](./LICENSE),

_AI Ghostfunctions_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from a fork of [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/bmritz/ai-ghostfunctions/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/bmritz/ai-ghostfunctions/blob/main/LICENSE
[contributor guide]: https://github.com/bmritz/ai-ghostfunctions/blob/main/CONTRIBUTING.md
[command-line reference]: https://ai-ghostfunctions.readthedocs.io/en/latest/usage.html
