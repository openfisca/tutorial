#!/bin/sh

.PHONY: all nb 

all: nb
nb:
	jupyter notebook *.ipynb
