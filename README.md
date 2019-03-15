# Learning Python

## First steps to master Python

Read the [Python tutorial](https://docs.python.org/3/tutorial/index.html) and transcribe and run the examples.
Once finished, have a look at the [The Hitchhiker’s Guide to Python!](https://docs.python-guide.org/).


## Resources

Great online resources for Python developers are among other things:

 * [The Python 3 Tutorial](https://docs.python.org/3/tutorial/index.html)
 * [Documentation for Python 3](https://docs.python.org/3/)
 * [The Hitchhiker’s Guide to Python!](https://docs.python-guide.org/)
 * [RealPython](https://realpython.com/)
 * [PyMOTW-3](https://pymotw.com/3/index.html)
 * [pythonspot.com - Python Tutorials](https://pythonspot.com/)
 * [LearnPython.org](https://www.learnpython.org/)
 * [FullStackPython.com](https://www.fullstackpython.com/)
 * [Awesome Python Github Repo](https://github.com/vinta/awesome-python)


## Libraries

Very useful Python libraries:
 
 * [asyncio](https://docs.python.org/3/library/asyncio.html)
 * [aio-libs](https://github.com/aio-libs)
 * [sqlalchemy](https://www.sqlalchemy.org/)


## Tools

 * [pipenv: python packaging tool](https://docs.pipenv.org/)
 * [pip: package manager for installing Python packages](https://pip.pypa.io/en/stable/)
 * [virtualenv: tool to create isolated Python environments.](https://virtualenv.pypa.io/en/stable/)
 * [pytest: testing tool](https://docs.pytest.org/en/latest/)
 * [ipython: interactive python shell](https://ipython.org/)


## Useful stuff to know

### Basic HTTP server
Python3 provides a built-in HTTP server which can be used to serve static files
on a development system.

```
python3 -m http.server 8080
```

### Virtualenv: basic workflow

1) Create a new Python project and create new virtual environment called .venv

```
mkdir project
virtualenv .venv -p python3.6
source .venv/bin/activate
```

2) Install dependencies and projects:

```
pip install -r requirements
```

```
pip install -e .
```

```
python setup.py install -e
```

3) Leave the virtual environment:

```
decativate
```


### pip

The table below provides the basic pip commands:

| Command                  | Description                      |
|:-------------------------|:---------------------------------|
| `pip install <pkg>`      | Install package `<pkg>`          |
| `pip uninstall <pkg>`    | Uninstall package `<pkg>`        |
| `pip freeze`             | Output installed packages in requirements format |
| `pip list`               | List installed packages |
| `pip show <pkg>`         | Show information about installed packages |
| `pip download <pkg>`     | Download package `<pkg>` |
| `pip search <term>`      | Search PyPI for package  |


### pipenv

```
pipenv --help

Usage: pipenv [OPTIONS] COMMAND [ARGS]...

Options:
  --update         Update Pipenv & pip to latest.
  --where          Output project home information.
  --venv           Output virtualenv information.
  --py             Output Python interpreter information.
  --envs           Output Environment Variable options.
  --rm             Remove the virtualenv.
  --bare           Minimal output.
  --completion     Output completion (to be eval'd).
  --man            Display manpage.
  --three / --two  Use Python 3/2 when creating virtualenv.
  --python TEXT    Specify which version of Python virtualenv should use.
  --site-packages  Enable site-packages for the virtualenv.
  --jumbotron      An easter egg, effectively.
  --version        Show the version and exit.
  -h, --help       Show this message and exit.


Usage Examples:
   Create a new project using Python 3.6, specifically:
   $ pipenv --python 3.6

   Install all dependencies for a project (including dev):
   $ pipenv install --dev

   Create a lockfile containing pre-releases:
   $ pipenv lock --pre

   Show a graph of your installed dependencies:
   $ pipenv graph

   Check your installed dependencies for security vulnerabilties:
   $ pipenv check

   Install a local setup.py into your virtual environment/Pipfile:
   $ pipenv install -e .

Commands:
  check      Checks for security vulnerabilities and...
  graph      Displays currently–installed dependency graph...
  install    Installs provided packages and adds them to...
  lock       Generates Pipfile.lock.
  open       View a given module in your editor.
  run        Spawns a command installed into the...
  shell      Spawns a shell within the virtualenv.
  uninstall  Un-installs a provided package and removes it...
  update     Uninstalls all packages, and re-installs...
```

#### Examples

Install a pip package:

```
pipenv install <package>
```

Uninstall a pip package:

```
pipenv uninstall <package>
```

Spawn subshell in the virtual environment:

```
pipenv shell
```

Create Python2 virtualenv:

```
pipenv --two
```

Create Python3 virtualenv:

```
pipenv --three
```

Remove virtualenv:

```
pipenv --rm
```

Show virtualenv:

```
pipenv --venv
```

