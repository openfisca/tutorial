# OpenFisca Tutorial

[OpenFisca](http://openfisca.org) is a versatile microsimulation free software.

Check the [online documentation](http://openfisca.org/doc/) for more details.

This package contains tutorials to test and explore OpenFisca.

## Notebooks

The tutorial notebooks of OpenFisca offer you an overview of how to compute with this microsimulation software. Use them to explore how it works !

Just click here to start:

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/openfisca/tutorial)

> This repository entails also the configuration files for the [Binder](http://mybinder.org/) which deploys a computational environment with the technology of [Jupyter](http://jupyter.org) Notebooks.

To install and launch a jupyter notebook locally:
 ```sh
cd notebooks
make install
make run
```

## Python

### [Python tutorials for OpenFisca-France](./python/)

With the Python [tutorials](./python/) (in French), you will learn how to:
- use the python API to run calculations
- get results on the current legislation as well as on [reforms](http://openfisca.org/doc/reforms.html)
- export results to .csv files

For more information, see this [README](./python/README.md) (in French).

### [Situations for OpenFisca-France](./python/situations)

This directory contains pre-filled input data, called situations, extracted from the French ["Livret du pouvoir d'achat"](https://www.economie.gouv.fr/files/files/PLF2018/bro-pouvoir-achat-bat-web-10h.pdf).

You can use them 'as is' in the web API or import them in the python API as shown in the python tutorials.

### [Python scripts for OpenFisca-France](./python/scripts)

- [`openfisca_json_customizer.py`](./python/scripts/openfisca_json_customizer.py) takes in an OpenFisca situation and customizes it thanks to a few helper methods.
- [`clean_mes_aides_situation.py`](./python/scripts/clean_mes_aides_situation.py) takes in a [Mes Aides](https://mes-aides.gouv.fr) situation and turns it into an OpenFisca-France situation.
- [`generate_situation_example`](./python/scripts/generate_situation_examples) contains the `situation_example package`, along with the `try_situation_examples.py` script. The `situation_examples` package contains complete cookie cutter situations (single, couple, roommates) that are ready to use in the python API, and the web API (in their json form)

To run one of the following scripts, go to its directory an call it with the `python` command.

### [Wiki](https://github.com/openfisca/tutorial/wiki)

A wiki provides additional information to this `tutorial` repository.

For technical tips on Python environment, see its [FAQ](https://github.com/openfisca/tutorial/wiki/FAQ) (in French).

## Examples

OpenFisca use cases:
* [French] Working group on rights and services access, fighting against non-uptake of social assistance in [./exemples/gt_non_recours](./exemples/gt_non_recours).
