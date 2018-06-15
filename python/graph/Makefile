#!/bin/bash

all: clean build

install:
	pip install dash==0.21.1  # The core dash backend
	pip install dash-renderer==0.13.0  # The dash front-end
	pip install dash-html-components==0.11.0  # HTML components
	pip install dash-core-components==0.23.0  # Supercharged components
	pip install plotly --upgrade  # Latest Plotly graphing library
	pip install OpenFisca-France<22.0.0

clean:
	find . -name '*.pyc' -exec rm \{\} \;

build:
	python app.py
