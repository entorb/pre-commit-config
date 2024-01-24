# pre-commit config for Python projects

Here is my config for pre-commit, Ruff and CSpell code checks.

Use case: performs automated code style checks (linting), formatting and spell check on a (python) git repository

## install pre-commit

`pip3 install pre-commit`

## configure pre-commit

see <https://pre-commit.com>

[.pre-commit-config.yaml](.pre-commit-config.yaml)

* defines and configures which hooks to run
* see <https://pre-commit.com/hooks.html> for complete list

## configure ruff hook (linter and formatter)

see <https://docs.astral.sh/ruff/>

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

## configure cspell hook (spell checker)

see <https://cspell.org>

* [cspell.json](cspell.json) config
* [cspell-words.txt](cspell-words.txt) custom dictionary

## run pre-commit manually

`pre-commit run --all-files`

or

`pre-commit run --files myFile1.py myFile2.json`

## run pre-commit automated upon each `git commit` command

`pre-commit install`

to install the hook so it will be executed upon each local `git commit` command.

## run pre-commit automated via GitHub Actions

Copy dir [.github/workflows/](.github/workflows/) to your repo, to automatically trigger the run upon push of commits and creation of pull requests.

## update pre-commit hooks to latest version

`pre-commit autoupdate`

to update versions of all hooks in [.pre-commit-config.yaml](.pre-commit-config.yaml) to the latest version.
