# -*- coding: utf-8 -*-

'''
france_situation_from_mesaides_to_openfisca_v20.py : Converts a MesAides situations to OpenFisca v20, in JSON format.

Usage :
  `france_situation_from_mesaides_to_openfisca_v20.py file.json`

where file.json is a MesAides situation in JSON format.
'''

import json
import sys

with open(sys.argv[1], 'r+') as f:
    data = json.load(f)
    data.pop(u'_id', None)
    f.seek(0)
    f.truncate()
    json.dump(data, f, indent=2, sort_keys=True)
