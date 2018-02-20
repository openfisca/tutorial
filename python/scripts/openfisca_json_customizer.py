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
from collections import OrderedDict
import dpath.util
from dpath.exceptions import PathNotFound 
import logging


# Main functions

handler = logging.StreamHandler()
log = logging.getLogger(__name__)
log.addHandler(handler)
log.setLevel(logging.DEBUG)


def update_json(json_file, update_actions):
  with open(json_file, 'r+') as f:
    json_content = json.load(f, object_pairs_hook=OrderedDict)
    update_actions(json_content)
    update_file(f, json_content)


def update_actions(json_content):
  log.info("Add in 'update_actions' function any action you want to apply to json_content.")
  
  # Point to a specific key using its name or its path (explore a json file like a file system)
  # For more information, see: https://pypi.python.org/pypi/dpath

  # E.g. : Updating the a key's value and printing it, assuming the key is u'_id' and the new value is 'toto'.
  # id_key = u'_id'
  # new_value = u'toto'
  # update_value(json_content, id_key, new_value)
  # print_value(json_content, id_key)


# Helpers

def is_json(file_path):
  return file_path[-5:] == ".json"


def print_value(json_content, key):
  try:
    log.info(key + u": " + str(dpath.util.get(json_content, key)))
  except KeyError as e:
    log.error(e.message + u' key non found.')


def print_json(json_content):
  log.info(json.dumps(json_content, indent=4, sort_keys=True))


def add_key(json_content, new_key, new_value):
  dpath.util.new(json_content, new_key, new_value)


def update_value(json_content, key, new_value):
  dpath.util.set(json_content, key, new_value)


def update_key(json_content, old_key, new_key, new_value):
  delete_key(json_content, old_key)
  add_key(json_content, new_key, new_value)


def delete_key(json_content, key):
  try:
    dpath.util.delete(json_content, key)
    log.debug(key + u' key deleted.')

  except KeyError as e:
    log.error(e.message)
  except PathNotFound as e:
    log.error(e.message)
      

def update_file(file, content):
  file.seek(0)
  file.truncate()
  file.write(json.dumps(OrderedDict(content), file, indent=4, sort_keys=True))
  file.write("\n")



if __name__ == "__main__":
  # Runs the modifying script on the json file
  try:
    update_json(sys.argv[1], update_actions)
  except BaseException as e:
    if len(sys.argv) == 1:
      log.error(u'Missing a .json file to customize.')
      log.warn(u'USAGE : python openfisca_json_customizer.py file.json')
    else:
      if e.message:
        log.error(str(e.__class__.__name__)+ ': ' + e.message)
      else:
        log.error(e)
