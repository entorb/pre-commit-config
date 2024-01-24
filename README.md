# pre-commit config for Python projects

Here is my config for pre-commit and Ruff.

Usecase: performs automated code style checks (linting) and formatting on a python git repository
see <https://pre-commit.com> and <https://docs.astral.sh/ruff/> for details.

## install

`pip3 install pre-commit`

## configure

add these files to your git repo:

[.pre-commit-config.yaml](.pre-commit-config.yaml)

* defines and configures which hooks to run
* see <https://pre-commit.com/hooks.html> for complete list

[.ruff.toml](.ruff.toml)

* configures the Ruff linter and formatter hook
* Ruff includes the features of these linters: flake8, pyupgrade and autoflake
* Ruff includes the features of these formatters: black, isort, add-trailing-comma
* Ruff offers a list of 700+ rules, see <https://docs.astral.sh/ruff/rules/> for list
* in my configuration I enabled most of them

To disable ruff checking of a (legacy) file or path, you can

* add a `# ruff: noqa` comment inside that file
* exclude via [.ruff.toml](.ruff.toml): `extend-exclude = ["src/MyFile1.py"]`
* exclude via [.pre-commit-config.yaml](.pre-commit-config.yaml)
* exclude via .gitignore file

## update pre-commit hooks to latest version

`pre-commit autoupdate`

to update versions of all hooks in [.pre-commit-config.yaml](.pre-commit-config.yaml) to the latest version

## run automated as pre-commit hook in your local git repository

`pre-commit install`

to install the hook so it will be executed upon each local `git commit` command

## run manually

`pre-commit run --all-files`

or

`pre-commit run --files myFile1.py myFile2.py`

## run automated via GitHub Actions

copy dir [.github/workflows/](.github/workflows/) to your repo, to automatically trigger the run upon push of commits and creation of pull requests.
