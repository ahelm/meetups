
---

# Should you use Python 2 or Python 3?

<!--

- **RAISE A HAND WHO IS WORKING WITH PYTHON 2.x**
- **RAISE A HAND WHO IS WORKING WITH PYTHON 3.x**

-->

---

# Use Python 3

---

# Python 2.7 will not be maintained past 2020

![Python 2.7 countdown](section_1/python2-7_countdown.png)

<!-- ---

# Features of Python 3

courtesy to

[Aaron Meurer's presentation "10 awesome features of Python that you can't use because you refuse to upgrade to Python 3"](https://www.asmeurer.com/python3-presentation/slides.html)

---

# Features of Python 3

- Advanced unpacking:

  ```python
  a, b, *rest = range(100)    # a = 0, b = 1, rest = [..]
  a, *rest, b = range(100)    # a = 0, b = 99, rest = [..]
  ```

---

# Features of Python 3


- Chained exceptions (in Python 2 you lost the traceback on the go):

  ```python
  def mycopy(source, dest):
      try:
          shutil.copy2(source, dest)
      except OSError: # We don't have permissions. More on this later
          raise NotImplementedError("automatic sudo injection")
  ```

---

# Features of Python 3

- More exceptions especially for `OSError`
- Almost everything is an iterator
  - speeds up code parts and reduces memory footprint
  - use `list()` to get a list out of an iterator

---

# Features of Python 3

- No more comparision of everything to everything

  ```python
  "abc" > 123
  # Python 2: True
  # Python 3: TypeError: '>' not supported between instances of 'str' and 'int'
  ```

---

# Features of Python 3

- caching of function calls `functools.lru_cache`
- Matrix multiplication with `@` operator
- `pathlib` in standard library for dealing with paths

---

# Features of Python 3

- Since Python 3.6, Python runs faster and is more economical with memory
- f-Strings: `print(f"some variable = {variable}")`
- asyncio: writing concurrent code
- type annotations -->

---

# Why use Python 2

## some library are **STILL** not compatible with Python 3

---

# Python packaging and tools

## Python package management

- **Pip:** pip is the package installer for Python
- **Pipenv:** is a tool that aims to bring the best of all packaging worlds
- **Poetry:** helps to declare, manage and install dependencies of Python
  projects, ensuring you have the right stack everywhere

---

# Python packaging and tools

## How about working with different python versions

- **Conda:** package, dependency and environment management for any
  language—Python, R, Ruby, Lua, Scala, Java, JavaScript, C/ C++, FORTRAN
- **Docker:** containerization for managing "dependency hell"

---

# Solving python version issues with Conda

- CLI tool which is used as a package management system and environment
  management system
- Cross-platform
- Pip on steroids (simplified)
- To install `conda`, either install
  [Anaconda](https://www.anaconda.com/distribution/) or
  [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

---

# Creating custom environment

- Like a `virtualenvwrapper` a separate "hidden" environment not to interact
  with your system python
- Resolves automatically dependencies and installs recipes and pre-build
  packages

```sh
conda create -n new_conda_environment python=2.6 django=1.6
```

---

# Activating custom conda environment

Listening all available `conda` environments:

```sh
conda info --envs
```

```
#conda environments:
base                   *  /Users/anton/miniconda3
new_conda_environment     /Users/anton/miniconda3/envs/new_conda_environment
```

---

# Activating an environment is easy as

Will set enviroment for you automatically

```sh
conda activate new_conda_environment
# will add `(<enviroment_name>)` in front of the prompt in the shell
```

---
# Each environment comes with an own `pip`

```sh
which pip
```

```
/Users/anton/miniconda3/envs/new_conda_environment/bin/pip
```

---

# Including the specified packages and version

Listing everthing available by pip

```sh
pip list
```

```
Django (1.6.6)
pip (7.1.0)
setuptools (18.0.1)
```

---

# Better to install new packages through `conda install`
## Pip as an alternative
