# Development

This package was created with Cookiecutter and the [rnwolf/py-cookiecutter](https://github.com/rnwolf/py-cookiecutter) project template.

This template should make it easier to develop python command line applications.

These applications are based on the [Typer](https://typer.tiangolo.com/) library.  They are packaged up using [Poetry](https://python-poetry.org/)

Testing of the app is done via [PyTest](https://docs.pytest.org/en/latest/).

The the application modifies images a Pytest fixture as discussed [here](https://redshiftzero.github.io/pytest-image/) is used to test that the application is not accidentlally broken during development.

As this is a new CLI application I am going for 100% testing coverage :

```
pytest --cov=imagetitle tests/
```


# Tips for Win 10 environment

If using Windows PowerShell terminal consider installing Set-PsEnv.psm1.
And then updating the virtualenv activate script because VSCode does not yet automatically load .env valiables in the Terminal, although they are loaded by the Python process.
https://github.com/microsoft/vscode-python/issues/944#issuecomment-458774142

```Get-ChildItem Env:``` To list environment vars in shell.

I am not using Pylint in VSCode it seems to raise some false errors.


# Fonts

## Tips for MacOS

The ```imagetitle``` application uses an "Ubuntu Condensed" font.  The following should enable you to install the font, at the terminal on MacOS.

```
cd ~/Library/Fonts && { curl -O 'https://meganerd.keybase.pub/ubuntu-font-family-0.83/Ubuntu-C.ttf' ; cd -; }
```

## Development Process Overview

Install the Github CLI tool **gh**.

https://github.com/cli/cli

Install the PlantUML utility to ensure that diagrams embeded in docs can be generated.
Check [instalation instructions.](https://pypi.org/project/plantuml-markdown/)
On windows use  `choco install plantuml` or `scoop install plantuml`

Install Vale, a writing style linter and the 'Google Writing Style Rules'

https://errata-ai.gitbook.io/vale/getting-started/installation

Get the release and place executable into file on the path such as C:\Users\rnwol\.local\bin

Make sure you have the lastest [Google Writting Style Rules](https://github.com/errata-ai/Google/releases)


Install pipx if not installed

```
python3 -m pip install pipx
python3 -m pipx ensurepath
```


Install cookiecutter

```pipx install cookiecutter```

Install virtualenv to make setting up environments MUCH faster

```pipx install virtualenv
virtualenv --help
```

Install poetry, package dependency management tool

```pipx install poetry```

Make sure to configure poetry to save virtualenv to a local .venv location, so that it can be found by VSCode and PyCharm.

```poetry config --local virtualenvs.in-project true```

Use cookiecutter to create project from this template

```pipx run cookiecutter gh:rnwolf/py-package-cookiecutter```

Answer cookiecutter qustions.

Enter Package directory

```cd overlay_image_title```

Initialise git repo
```git init```

Ensure that make-linux-release.sh file is executable.

On  MS-Windows use :  ```git add --chmod=+x -- make-linux-release.sh```
On Linux : ```chmod + x make-linux-release.s```

Add and commit files.

```
git add --all
git commit -m "First commit"
```

Create a repository for the current directory with GitHub GH cli utility.

```gh repo create --public```

Connect up local and remote repo. -u = upstream

```git push -u origin master```

Create virtualenv (Have some problems doing this with poetry)

```py -3.8 -m venv .venv```  #Windows
or
```python3.8 -m venv .venv```
or use https://virtualenv.pypa.io/en/latest/
```virtualenv -p 3.8 .venv```

Install all dependencies specified in pyproject.toml

```poetry install```

Setup pre-commit and pre-push hooks

```
poetry run pre-commit install -t pre-commit
poetry run pre-commit install -t pre-push
```

Launch IDE, like VSCode

Ctrl+Shift P  -> Select Interperter, Testing, Linting etc.

Specify what the next version is that will be worked on.
bump current version with, bump rule:
 - patch, minor, major, prepatch, preminor, premajor, prerelease.

For example:

```poetry version patch```

Create a GitHub Issue and document what the intention of the planned change is.

```gh issue create```

Make a note of the issue number, to be used with the change note.
Make a end user focused note of the change in the folder.

```.\changes\feature\issue.<issue number>.md```

Add tests in the .\tests folder.

Make sure you use the utilities installed to ensure quality.

```pytest  # Run all automated tests
pytest --cov=imagetitle tests # Look for 100% coverage
```
Pin point which parts of the code are NOT covered by a test.

```
pytest --cov-report term-missing:skip-covered --cov=imagetitle .\tests\
```

Auto format code and tests

```
black tests
black imagetitle
```

```
flake8  # All sorts of guidance
interrogate   # Docstring check
safety check  # Check dependent packages for security adviories

pre-commit run --all-files  # Run all the CI lint tests, including black for auomatic layout

vale .\docs  # Check the quality of your documentation
```

Run and test your application in the following ways:

```
imagetitle --help
python -m imagetitle --help
pytest
```

Update DOCUMENTAION before you build the package.

To preview documentation change summary use:

```proclamation build YOUR_NEW_VERSION_NUMBER```

To overwrite your changelog file with the updated one and delete the used changelog fragments.

```
proclamation build YOUR_NEW_VERSION_NUMBER --delete-fragments --overwrite
```

Update DOCUMENTAION before you build the package.
Use Typer superpowers to build documentation based on DocStrings and Typer configuration

```
typer imagetitle.imagetitle utils docs --name imagetitle --output docs/autodoc.md
```

Check that the documentation is good.
`mkdocs build` or `mkdocs serve` commands to build and review the documentation.

Add the changed files

```
git add
git commit -m "My comment"
```

If you have several commits to squash together do the following.

```
git log
git rebase --interactive [commit-hash]
```
mark all the commits as squashable, except the first/older one
mark a commit as squashable by changing the work pick into squash next to it (or s for brevity)

Use Typer to generate the documentation for the Readme files.

```typer .\src\imagetitle\imagetitle.py utils docs --name imagetitle --output ./docs/help.md```

Copy the output of help.md into the README.MD and index.md files.

OPTIONAL

Publish the documentation to the GH-Pages at
```
http(s)://<github_user>.github.io/<repository_name>
```

Note: It takes a few minutes for the pages to apprear.
https://rnwolf.github.io/imagetitle/

```
mkdocs gh-deploy # Subsequent commits to repo will automatically publish gh-pages with action workflow.
```

Commit tested code and reviewed documentation.
```
git commit -m "What was added?"
git push
```

To create local build of the package
add a VERSION_NUMBER as a semver tag. Based on version value in pyproject.toml
Check with: grep ^version pyproject.toml

```
git tag v0.0.1
git push --tags  # Tags have to be explicitly pused to the remote origin git repo.
```

Remove the previous build artefacts

```rm -rf dist build```

or

```
PS> Remove-Items -force -r dist
poetry build # Build release package
```

Add the TestPyPI repository to Poetry. The default location is to the real PyPI.
poetry config repositories.test-pypi https://test.pypi.org/legacy/

Publish, enter username and password
Better to use tokens for a specific package if you can. https://pypi.org/help/#apitoken

```poetry publish -r test-pypi```

Add PyPI repo to Poetry, with the use of a token, rather than password.

```poetry config pypi-token.pypi my-token```

Or TEST release process to a LOCAL PRIVATE Devlopment PyPi instance.

Reference:

https://github.com/python-poetry/poetry/issues/726#issuecomment-598392820
https://stefan.sofa-rockers.org/2017/11/09/getting-started-with-devpi/

Setup a local Development PyPi to test the upload of releases with poetry
NOTE CANNOT Use Python 3.8. Works with Python 3.7.

If installing on a clean Ubuntu server then

```
apt-get -y update
apt-get install -y python3-venv libssl-dev libffi-dev python3-dev build-essential
```

Create working directory
```
cd ~
cd workspace  # or similar WIP directory
mkdir mypypi
```

Create Virtualenv

```
python3.7 -m venv .venv
./.venv/bin/python -m pip install pip --upgrade
source ./.venv/bin/activate
pip install devpi-web devpi-client
devpi-init
devpi-gen-config

apt install -y supervisor
supervisord -c gen-config/supervisord.conf

devpi use http://localhost:3141
devpi login root  #root password is blank!
```

Create a "packages" user & index.

```
devpi user -c packages email=packaging@company.com password=packages
devpi index -c packages/stable bases=root/pypi volatile=False
```

Add information about the DevPyPi server/service

```
poetry config repositories.stable http://localhost:3141/packages/stable

poetry publish -r stable -u ${username} -p {password}
poetry publish -r stable -u packages -p packages
```

Check index in your browser
http://localhost:3141/packages/stable

FINALY
Download the CI package artefacts wheel and tar file, to local folder called ./dist
Edit the release info in github and upload the release package artefacts.

```poetry publish   # To publish packages aretefacts to PyPi```

## Docker Image

Build Image with

```
docker build --pull --rm -f "Dockerfile" -t overlayimagetitle:latest "."
```

Run the code in the Docker image with:

In Windows Powershell with (The volumn mapping to PWD directory varies depending on OS.)

```
docker run -t -i --rm -v ${PWD}:/usr/app overlayimagetitle:latest -i /usr/app/input.png -o /usr/app/out.png --font="/fnt/Ubuntu-C.ttf"
```

In order to get inside the Docker image use the following:

```
docker run -t -i --rm -v ${PWD}:/app overlayimagetitle:latest

```



## CHANGELOG / NEWS entries

The docs/changelog.md file is managed using pronouncments and all non trivial changes must be accompanied by a news entry. To add an entry to the changelog.md file, first you need to have created a repo issue describing the change you want to make. A Pull Request itself may function as such, but it is preferred to have a dedicated issue (for example, in case the PR ends up rejected due to code quality reasons).

Once you have an issue or pull request, you take the number and you create a file inside of the changes directory.

Thus if your issue or PR number is 1234 and this change is fixing a bug, then you would create a file docs/changelog/bugfix/1234.md . PRs can span multiple categories by creating multiple files (for instance, if you added a feature and deprecated/removed the old feature at the same time, you would create docs/changelog/bugfix/1234.md and docs/changelog/remove/1234.md). Likewise if a PR touches multiple issues/PRs you may create a file for each of them with the same contents and pronouncment will deduplicate them.

### Contents of a NEWS entry

The contents of this file are markdown formatted text that will be used as the content of the news file entry. You do not need to reference the issue or PR numbers here as pronouncement will automatically add a reference to all of the affected issues when rendering the news file.

In order to maintain a consistent style in the CHANGELOG.md file, it is preferred to keep the news entry to the point, in sentence case, shorter than 120 characters and in an imperative tone – an entry should complete the sentence This change will …. In rare cases, where one line is not enough, use a summary line in an imperative tone followed by a blank line separating it from a description of the feature/change in one or more paragraphs, each wrapped at 120 characters. Remember that a news entry is meant for end users and should only contain details relevant to an end user.
