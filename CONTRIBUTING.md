# Contributor Guide

Thank you for your interest in improving this project.
This project is open-source under the [MIT license] and
welcomes contributions in the form of bug reports, feature requests, and pull requests.

Here is a list of important resources for contributors:

- [Source Code]
- [Documentation]
- [Issue Tracker]
- [Code of Conduct]

[mit license]: https://opensource.org/licenses/MIT
[source code]: https://github.com/bmritz/ai-ghostfunctions
[documentation]: https://ai-ghostfunctions.readthedocs.io/
[issue tracker]: https://github.com/bmritz/ai-ghostfunctions/issues

## How to report a bug

Report bugs on the [Issue Tracker].

When filing an issue, make sure to answer these questions:

- Which operating system and Python version are you using?
- Which version of this project are you using?
- What did you do?
- What did you expect to see?
- What did you see instead?

The best way to get your bug fixed is to provide a test case,
and/or steps to reproduce the issue.

## How to request a feature

Request features on the [Issue Tracker].

## How to improve documentation

To get a live-reloading version of the documentation locally, run:
`NOXSESSION=docs make run-nox-session`.

Make your changes in the `docs/` folder.

## How to set up your development environment

You need Python 3.8+ and the following tools:

- [poetry](https://python-poetry.org/)
- [nox](https://nox.thea.codes/)
- [nox-poetry](https://nox-poetry.readthedocs.io/)

Install the package with development requirements:

```console
$ make install
```

You can now run an interactive Python session:

```console
$ .poetry/bin/poetry run python
```

## How to test the project

Run the full test suite:

```console
$ make run-nox-all
```

List nox sesssions:

```console
$ .poetry/bin/poetry run nox --list
```

You can also run a specific Nox session.
For example, invoke the unit test suite like this:

```console
$ NOXSESSION=<session-name> make run-nox-session
```

Unit tests are located in the _tests_ directory,
and are written using the [pytest] testing framework.

[pytest]: https://pytest.readthedocs.io/

## How to submit changes

Open a [pull request] to submit changes to this project.

Your pull request needs to meet the following guidelines for acceptance:

- The Nox test suite must pass without errors and warnings.
  - Assert this with `make run-nox-all`
- Include unit tests. This project maintains reasonable code coverage.
- If your changes add functionality, update the documentation accordingly.

Feel free to submit early, though—we can always iterate on this.

To run linting and code formatting checks before committing your change, you can install pre-commit as a Git hook by running the following command:

```console
$ NOXSESSION='pre-commit -- install' make run-nox-session
```

It is recommended to open an issue before starting work on anything.
This will allow a chance to talk it over with the owners and validate your approach.

[pull request]: https://github.com/bmritz/ai-ghostfunctions/pulls

<!-- github-only -->

[code of conduct]: CODE_OF_CONDUCT.md

## To release a new version

git checkout main
git pull
make new-version-<patch|minor|major|prepatch|preminor|premajor|prerelease>
git add pyproject.toml
git commit -m 'release new version'
git push
