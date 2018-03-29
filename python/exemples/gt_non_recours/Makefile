#!/bin/bash

.PHONY: all install run clean

all: run

install:
	pip install -r requirements.txt

run:
	python framework.py

clean:
	find . -name '*.pyc' -exec rm \{\} \;
