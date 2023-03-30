REQUIRED := python3
$(foreach bin,$(REQUIRED),\
    $(if $(shell command -v $(bin) 2> /dev/null),,$(error Please install `$(bin)`)))

REPOSITORY_ROOT := $(PWD)

help:	## Show this help. (Default target)
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help

.PHONY : install install-poetry run-nox-all run-nox-session format run-quick-test ipython-shell

install-poetry: .poetry/bin/poetry	## Install poetry in the project.
	$< install

install: install-poetry		## install all dependencies for development
	NOXSESSION='pre-commit -- install' make run-nox-session

.poetry/bin/poetry:						## install poetry
	@curl -sSL https://install.python-poetry.org | POETRY_HOME=$(REPOSITORY_ROOT)/$(shell basename $(dir $(abspath $(dir $(@))))) python3 - --version=1.4.0
	$(MAKE) install-poetry

run-nox-all: .poetry/bin/poetry			## Run all nox sessions
	PATH=$$PATH:$(dir $<) $< run nox

run-nox-session: .poetry/bin/poetry guard-NOXSESSION			## Run a specific nox session. Call via something like NOXSESSION=tests-3.10 make run-nox-session
	# nox needs poetry, so we need to put poetry on the path
	PATH=$$PATH:$(dir $<) $< run nox -- -s $(NOXSESSION)

list-of-nox-sessions-print: .poetry/bin/poetry
	$< run nox --list

run-quick-test: .poetry/bin/poetry			## Run all nox sessions
	$< run pytest

ipython-shell: .poetry/bin/poetry	## Fire up an ipython shell with dependencies available in the environment.
	$< run ipython

format: .poetry/bin/poetry	## Format the code by running isort and black on the repo.
	$< run isort .
	$< run black .

new-version-%: .poetry/bin/poetry	## Make a new version. Use: make new-version-<patch|minor|major|prepatch|preminor|premajor|prerelease>
	$< version -- $*

guard-%: .poetry/bin/poetry		## Used to ensure an env var is available for a target that depends on guard-%
	@if [ -z '${${*}}' ]; then echo 'Variable $* not set. You can set it with $*=VALUE make ...' && exit 1; fi
