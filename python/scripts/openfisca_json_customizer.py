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


# Main functions

def update_json(json_file):
  with open(json_file, 'r+') as f:
    json_content = json.load(f)
    update_actions(json_content)
    update_file(f, json_content)


def update_actions(json_content):
  # E.g. : Mise à jour de la valeur d'id et vérification de succès
  id_key = u'_id'
  # json_content = update_value(json_content, id_key, u'toto')
  # print_value(json_content, id_key)

  # E.g. : Suppression d'id et vérification de succès
  json_content = delete_key(json_content, id_key)
  print_value(json_content, id_key)


# Helpers


def print_value(json_content, key):
  try:
    print key + ": " + dpath.util.get(json_content, key)
  except KeyError as e:
    print 'Clef ' + e.message + ' introuvable.'


def print_json(json_content):
  print json.dumps(json_content, indent=4, sort_keys=True)


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
    json_content.pop(key, None)
  except KeyError as e:
    print 'Clef ' + e.message + ' introuvable.'
  return json_content
      

def update_file(file, content):
  file.seek(0)
  file.truncate()
  file.write(json.dumps(content, file, indent=4, sort_keys=True))


# Runs the modifying script on the json file

update_json(sys.argv[1])
