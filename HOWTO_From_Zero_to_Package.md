# Creating a Python Package

Install poetry from pip:

## Installation

```bash
pip install poetry
```

```bash
poetry config virtualenvs.in-project true
```

### Give it a check, and see the **virtualenvs.in-project** by running

```bash
poetry config --list
```

One can initialize poetry

```bash
poetry init
```

### Create a new project with directory name as the package name

```bash
mkdir ai_bundle
poetry new .
```

### Create a Virtual Environment by running poetry install

```bash
poetry install
```

```bash
git init
git add *
git commit -m "First commit"
git branch -M main
git remote add origin https://github.com/alkhawli/ai_bundle.git
git pull origin main  --allow-unrelated-histories
git push -u origin main
```

### Set up some pre-commit hooks

Install pre-commit hook as a development dependency with Poetry:

```bash
poetry add -D pre-commit
```

Commit the updated dependencies:

```bash
git add poetry.lock pyproject.toml
git commit -m "Add pre-commit devt dependency."
```

Now, to set up pre-commit, we create a file .pre-commit-config.yaml in the root directory, and we just set it up how we want. This is how my .pre-commit-config.yaml file looks like:

```bash
# See https://pre-commit.com for more information
# See https://pre-commit.com/hooks.html for more hooks
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.0.1
    hooks:
      - id: check-toml
      - id: check-yaml
      - id: end-of-file-fixer
      - id: mixed-line-ending
  - repo: https://github.com/psf/black
    rev: 22.3.0
    hooks:
      - id: black
  - repo: https://github.com/PyCQA/isort
    rev: 5.10.1
    hooks:
      - id: isort
        args: ["--profile", "black"]
```

Afterwards, install the hooks run them.

```bash
pre-commit install
pre-commit run all-files
```

Make sure the Poetry virtual environment is active! if not run the command  *poetry shell*.

Commit the shanges by running:

```bash
git add pyproject.toml poetry.lock .pre-commit-config.yaml
git commit -m "Add pre-commit devt dependency."
git add *
git commit -m "Run all pre-commits."
git push
```

## Add a license

The MIT license is currently being selected.

## Test uploading the package

Test the package with the test PyPI repository, <https://test.pypi.org>. This lets everyone test their packaging/publishing workflows without messing with the real repository.

### Configure the test repository in Poetry

```bash
poetry config repositories.testpypi <https://test.pypi.org/legacy/>
```

This is to make Poetry aware of that repository, which we called testpypi.

### Get an API key

Get an API key so that Poetry can actually push to the testpypi repository. An  account on TestPyPI is required for this, and then a new API key under your account settings can be generated.

Use the API key in the command:

```bash
poetry config http-basic.testpypi __token__ pypi-your-api-token-here
```

### Build and upload your package

```bash
poetry build
poetry publish -r testpypi
```

The package `ai_bundle` should be live on TestPyPI.

Ignore the build products in the , which are generated in the dist folder, when commiting to Github. Just add this to the .gitignore file

## Populate the real package

Populate the package with the actual code, and then publish it to the real PyPI repository.

### Changelog management

For an efficient changelog management, *scriv* will be used. *Scriv* is a command-line tool for helping developers maintain useful changelogs. Add scriv to the development dependency with Poetry is straightforward:

```bash
poetry add -D scriv[toml]
```

Create a changelog.d folder in the directory, add .gitkeep file into it.

```bash
scriv create
```

Once the create command is executed, an md file with date time is created in the changelog.d folder. Uncomment the ***Added*** section and add the changes, for example:

- Classes `A` and `B` are implemented with the following functionality.

Save and commit all the changes.

### Publish the real package

Similar to publishting to the test PyPI, we can now publish it to the real PyPI repository! Simply go to the PyPI account (create one if needed!), grab an API key, and configure it in Poetry:

```bash
poetry config pypi-token.pypi pypi-your-token-here
```

### Build and publish

```bash
poetry publish --build
```

If things work well, one can just install it from pypi by executing this command: python -m pip install ai_bundle.

## Publish a Release

Edit the README file, describe the functionality. To collect all the changes from the changelog.d files, Run the following command:

```bash
scriv collect
```

Add the CHANGELOG.md to the README file example: Refer to the "["CHANGELOG.md"]"(CHANGELOG.md) file.

poetry add -D pytest

### Tag and Push the version in git

```bash
git tag -a v0.1.1 -m "Added all the changes to a 100% testing coverage"
push origin v0.1.1
```

The last step can be done by publish a release.

So the process in general will be:

1. scriv create
1. Edit changes in the changelog folder
1. Git add and commit
1. scriv collect
1. Tag version and Push
1. Generate tests
1. Repeat untill ready

## Write tests

Write tests and executes with command ```pytest``` command.

## Automating testing, linting, and formatting

Add ```tox.ini``` file to the project:

```tox.ini
[tox]
isolated_build = True
envlist = py310

[testenv]
deps =
    black
    coverage
    flake8
    mccabe
    mypy
    pylint
    pytest
commands =
    black podsearch
    flake8 podsearch
    pylint podsearch
    mypy podsearch
    coverage erase
    coverage run --include=podsearch/* -m pytest -ra
    coverage report -m
```

Run the tox file with this command:

```bash
tox
```

After running make sure a coverage 100% is reached. Once yes, build, tag, and publish.
