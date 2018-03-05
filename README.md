# OpenFisca Tutorial

[OpenFisca](http://openfisca.org) is a versatile microsimulation free software.  
Check the [online documentation](http://openfisca.org/doc/) for more details.

This package contains tutorials to test and explore OpenFisca.

## Notebooks

The tutorial notebooks of OpenFisca offer you an overview of how to compute with this microsimulation software. Use them to explore how it works !

Just click here to start:  
[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/openfisca/tutorial)   

> This repository entails also the configuration files for the [Binder](http://mybinder.org/) which deploys a computational environment with the technology of [Jupyter](http://jupyter.org) Notebooks.

## Python

### [Python tutorials for OpenFisca-France](./python/)

With the Python [Tutorials](./python/) (in French), you will learn how to:
- use the python API to run calculations
- get results on the current legislation as well as on reforms
- export calculation result to CSV

### [Situations for OpenFisca-France](./python/situations)
This directory contains pre-filled situations extracted from the French "Livret du pouvoir d'achat".

You can use them 'as is' in the web API or import them in the python API as shown in the python tutorials. 

### [Python scripts for OpenFisca-France](./python/scripts)
- [`openfisca_json_customizer.py`](./python/scripts/openfisca_json_customizer.py) takes in an OpenFisca situation and customizes it thanks to a few helper methods.
- [`clean_mes_aides_situation.py`](./python/scripts/clean_mes_aides_situation.py) takes in a [Mes Aides](https://mes-aides.gouv.fr) situation and turns it into an OpenFisca-France situation.
- [`generate_situation_example`](./python/scripts/generate_situation_examples) contains the `situation_example package`, along with the `try_situation_examples.py` script. The `situation_example package` contains complete cookie cutter situations (single, couple, roommates) thant are ready to use in the python API, and the web API (in their json form) 
