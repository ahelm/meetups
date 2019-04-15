<!--
TODO: move this file to the corresponding meetup folder
-->
# Python meetup presentation

## About me

- working with Python for ~11 years (mostly Numpy, Matplotlib, Cython, ...)
- "European polygot"
- PhD student in Physics at Instituto Superior Tecnico (IST)
- working on numerical simulations of plasmas
- numerical simulations are based on Fortran and run on up to 2M CPUs and
also GPUs
- Hobbies: Things, ...

## Disclaimer

- The things discussed in this meetup are not presenting anything related with
my research, my PhD or my day-to-day working schedule.

- This presentation is build up based on three major questions which
"hopefully" are up to now unanswered for your.

- Each section will try to cover a little bit of content connected with this
question and will give some insight to educate and enlighten the audience.

- After the presentation you should basically have a deeper understanding
about Python as a programming language and hopefully it will provide you with
some insights for future steps you are trying to achieve with Python.

## ☛ __Should you use Python 2 or Python 3?__

- **RAISE A HAND WHO IS WORKING WITH PYTHON 2.x**
- **RAISE A HAND WHO IS WORKING WITH PYTHON 3.x**

> You should work with Python 3.x

## Python 2.7 will not be maintained past 2020

- show link or screenshot of [Python 2.7 clock](https://pythonclock.org/)

## Pro's and con's to use Python 3.x vs. Python 2.x

Pro's for using Python 3:

- Advanced unpacking:

  ```python
  a, b, *rest = range(100)    # a = 0, b = 1, rest = [..]
  a, *rest, b = range(100)    # a = 0, b = 99, rest = [..]
  ```

- Chained exceptions (in Python 2 you lost the traceback on the go)

  ```python
  def mycopy(source, dest):
      try:
          shutil.copy2(source, dest)
      except OSError: # We don't have permissions. More on this later
          raise NotImplementedError("automatic sudo injection")
  ```

- More exceptions especially for `OSError`
- Everything is an iterator
  - speeds up some code parts and reduced memory footprint
  - use `list()` to get a list out of an iterator
- No more comparision of everything to everything

  ```python
  "abc" > 123
  # Python 2: True
  # Python 3: TypeError: '>' not supported between instances of 'str' and 'int'
  ```

- caching of function calls `functools.lru_cache`
- Matrix multiplication with `@` operator
- `pathlib` in standard library for dealing with paths

> courtesy to [
> Aaron Meurer's presentation "10 awesome features of Python that you can't use
> because you refuse to upgrade to Python 3"](
> https://www.asmeurer.com/python3-presentation/slides.html)

- Since Python 3.6, Python runs faster and is more economical with memory
- f-Strings: `print(f"some variable = {variable}")`

Pro's for using Python 2:

- some library are **STILL** not compatible with Python 3

## Python packaging and tools

### Python package management

- **Pip:** pip is the package installer for Python
- **Pipenv:** is a tool that aims to bring the best of all packaging worlds
- **Poetry:** helps to declare, manage and install dependencies of Python
  projects, ensuring you have the right stack everywhere

### Python package management++

- **conda:** Package, dependency and environment management for any
  language—Python, R, Ruby, Lua, Scala, Java, JavaScript, C/ C++, FORTRAN

## Solving python version issues with Conda

- explain the context of enviroment
- how to create a new enviroment
- how to specify a python version and specific version of a package
- how to activate the enviroment

## ☛ __Is Python a compiled or interpreted programming language?__

- **RAISE A HAND IF YOU THINK IT'S COMPILED**
- **RAISE A HAND IF YOU THINK IT'S INTERPRETED**
- **RAISE A HAND IF YOU THINK IT'S BOTH**

## ☛ __Is Python slow?__