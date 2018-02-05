# -*- coding: utf-8 -*-

'''
france_situation_from_mesaides_to_openfisca_v20.py : Converts a MesAides situations to OpenFisca v20, in JSON format.

Usage :
  `python france_situation_from_mesaides_to_openfisca_v20.py file.json`

where file.json is a MesAides situation in JSON format.
'''

import json
import sys
import dpath.util


# Fonctions principales

def update_json(json_file):
  with open(json_file, 'r+') as f:
    json_content = json.load(f)
    update_actions(f, json_content)
    update_file(f, json_content)


def update_actions(file_stream, json_content):
  # Ex : Mise à jour de la valeur d'id et vérification de succès
  id_key = u'_id'
  json_content = update_value(json_content, id_key, u'toto')
  print_value(json_content, id_key)

  # Ex : Suppression d'id et vérification de succès
  json_content = delete_key(file_stream, json_content, id_key)
  print_value(json_content, id_key)


# Fonction auxilaires


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


# Path rather than key ? ex : 'a/b/e/f/g'
def update_key(json_content, old_key, new_key, new_value):
  json_content = delete_key(json_content, old_key)
  json_content = add_key(json_content, new_key, new_value)
  return json_content


def delete_key(file_stream, json_content, key):
  try:
    json_content.pop(key, None)
  except KeyError as e:
    print 'Clef ' + e.message + ' introuvable.'
  return json_content
      

def update_file(file, content):
  file.seek(0)
  file.truncate()
  file.write(json.dumps(content, file, indent=4, sort_keys=True))


# Exécution de la mise à jour

update_json(sys.argv[1])
