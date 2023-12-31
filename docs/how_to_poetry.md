# Poetry:
https://python-poetry.org/docs/basic-usage/


## Project setup

```
poetry new poetry-demo
```

This will create the poetry-demo directory with the following content:



## Initialising a pre-existing project

Instead of creating a new project, Poetry can be used to ‘initialise’ a pre-populated directory. 
To interactively create a pyproject.toml file in directory pre-existing-project:

```
cd pre-existing-project
poetry init
```


## Specifying dependencies
If you want to add dependencies to your project, you can specify them in the tool.poetry.dependencies section.
```
[tool.poetry.dependencies]
pendulum = "^2.1"
```

Also, instead of modifying the pyproject.toml file by hand, you can use the add command.
```
poetry add pendulum
```

## Using your virtual environment
By default, Poetry creates a virtual environment in {cache-dir}/virtualenvs. You can change the cache-dir 
value by editing the Poetry configuration. Additionally, you can use the virtualenvs.in-project configuration 
variable to create virtual environments within your project directory.

There are several ways to run commands within this virtual environment.


## External virtual environment management

Poetry will detect and respect an existing virtual environment that has been externally activated. 
This is a powerful mechanism that is intended to be an alternative to Poetry’s built-in, simplified 
environment management.

To take advantage of this, simply activate a virtual environment using your preferred method or tooling, 
before running any Poetry commands that expect to manipulate an environment.


# Using poetry run
To run your script simply use poetry run python your_script.py. Likewise if you have command line tools 
such as pytest or black you can run them using poetry run pytest.


## Activating the virtual environment
The easiest way to activate the virtual environment is to create a nested shell with poetry shell.

To deactivate the virtual environment and exit this new shell type exit. To deactivate the virtual environment 
without leaving the shell use deactivate.


### Why a nested shell?

Child processes inherit their environment from their parents, but do not share them. As such, any modifications 
made by a child process is not persisted after the child process exits. A Python application (Poetry), being a 
child process, cannot modify the environment of the shell that it has been called from such that an activated 
virtual environment remains active after the Poetry command has completed execution.

Therefore, Poetry has to create a sub-shell with the virtual environment activated in order for the subsequent 
commands to run from within the virtual environment.


# Installing dependencies
To install the defined dependencies for your project, just run the install command.

```
poetry install
```
When you run this command, one of two things may happen:

## Installing without poetry.lock
Installing without poetry.lock
If you have never run the command before and there is also no poetry.lock file present, Poetry simply resolves 
all dependencies listed in your pyproject.toml file and downloads the latest version of their files.

When Poetry has finished installing, it writes all the packages and their exact versions that it downloaded to 
the poetry.lock file, locking the project to those specific versions. You should commit the poetry.lock file to 
your project repo so that all people working on the project are locked to the same versions of dependencies 
(more below).


## Installing with poetry.lock
This brings us to the second scenario. If there is already a poetry.lock file as well as a pyproject.toml 
file when you run poetry install, it means either you ran the install command before, or someone else on 
the project ran the install command and committed the poetry.lock file to the project (which is good).

Either way, running install when a poetry.lock file is present resolves and installs all dependencies that 
you listed in pyproject.toml, but Poetry uses the exact versions listed in poetry.lock to ensure that the 
package versions are consistent for everyone working on your project. As a result you will have all dependencies 
requested by your pyproject.toml file, but they may not all be at the very latest available versions 
(some dependencies listed in the poetry.lock file may have released newer versions since the file was created).
This is by design, it ensures that your project does not break because of unexpected changes in dependencies.


