# -*- coding: utf-8 -*-

'''
openfisca_json_customizer.py : Customizes a OpenFisca JSON situations.

Input :
  file.json is a Openfisca JSON situation to be updated (delete a key, change a period ...)

Usage :
  Define how you wish to modify your json file in `update_actions`. You can use the helpers defined in this file.
  then run :
  `python openfisca_json_customizer.py file.json`

Output :
  file.json, modified but whatever you defined in update action
where file.json is an OpenFisca situation in JSON format.

'''

import json
import sys
import dpath.util
from dpath.exceptions import PathNotFound 
import logging


# Main functions

handler = logging.StreamHandler()
log = logging.getLogger(__name__)
log.addHandler(handler)
log.setLevel(logging.DEBUG)


def update_json(json_file):
  with open(json_file, 'r+') as f:
    json_content = json.load(f)
    update_actions(json_content)
    update_file(f, json_content)


def update_actions(json_content):
  # E.g. : Updating '_id' key value and priting it
  # id_key = u'_id'
  # json_content = update_value(json_content, id_key, u'toto')
  # print_value(json_content, id_key)

  # E.g. : Updating json content from mes-aides.gouv.fr application structure to openfisca
  from_mesaides_to_openfisca(json_content)


def from_mesaides_to_openfisca(json_content):
  '''
  Removing mes-aides.gouv.fr application keys from given json content.
  '''
  id_key = u'_id'

  paris_keys = ['paris_complement_sante', 
    'paris_energie_famille', 'paris_forfait_famille', 
    'paris_logement', 'paris_logement_familles', 
    'paris_logement_aspeh', 'paris_logement_plfm', 'paris_logement_psol',
    'parisien']

  transport_keys = ['brest_metropole_transport', 'rennes_metropole_transport']

  json_content = delete_key(json_content, id_key)

  for key in paris_keys:
    json_content = delete_key(json_content, 'familles/_/' + key)
  
  for key in transport_keys:
    print_value(json_content, 'individus/demandeur/' + key)
    json_content = delete_key(json_content, 'individus/demandeur/' + key)
    json_content = delete_key(json_content, 'individus/enfant_0/' + key)


# Helpers


def print_value(json_content, key):
  try:
    log.info(key + u": " + str(dpath.util.get(json_content, key)))
  except KeyError as e:
    log.error(e.message + u' key non found.')


def print_json(json_content):
  log.info(json.dumps(json_content, indent=4, sort_keys=True))


def add_key(json_content, new_key, new_value):
  dpath.util.new(json_content, new_key, new_value)
  return json_content


def update_value(json_content, key, new_value):
  dpath.util.set(json_content, key, new_value)
  return json_content


def update_key(json_content, old_key, new_key, new_value):
  json_content = delete_key(json_content, old_key)
  json_content = add_key(json_content, new_key, new_value)
  return json_content


def delete_key(json_content, key):
  try:
    dpath.util.delete(json_content, key)
    log.debug(key + u' key deleted.')

  except KeyError as e:
    log.error(e.message + u' key not found.')
  except PathNotFound as e:
    log.error(e.message + u' path not found.')
  return json_content
      

def update_file(file, content):
  file.seek(0)
  file.truncate()
  file.write(json.dumps(content, file, indent=4, sort_keys=True))


# Runs the modifying script on the json file

try:
  update_json(sys.argv[1])
except BaseException as e:
  if len(sys.argv) == 1:
    log.error(u'Missing a .json file to customize.')
    log.warn(u'USAGE : python openfisca_json_customizer.py file.json')
  else:
    log.error(str(e.__class__.__name__)+ ': ' + e.message)
