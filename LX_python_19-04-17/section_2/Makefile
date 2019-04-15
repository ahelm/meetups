.PHONY: compile
compile: python_compiler.py
		docker run -it --rm -v "$(PWD)":/usr/src -w /usr/src python:3.7 python python_compiler.py

