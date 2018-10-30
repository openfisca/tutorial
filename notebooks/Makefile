#!/bin/bash

all: test

install:
	pip install -r requirements.txt

test: clean
	python test_notebooks.py .

clean:
	rm executed_*
