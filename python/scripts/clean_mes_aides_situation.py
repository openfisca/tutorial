import sys
import os.path
import logging

from openfisca_json_customizer import is_json, update_json, delete_key


handler = logging.StreamHandler()
log = logging.getLogger(__name__)
log.addHandler(handler)
log.setLevel(logging.DEBUG)


def from_mesaides_to_openfisca(json_content):
  '''
  Removing mes-aides.gouv.fr application keys from given json content.
  '''

  json_content = delete_key(json_content, u'_id')

  paris_keys = ['paris_complement_sante', 
    'paris_energie_famille', 'paris_forfait_famille', 
    'paris_logement', 'paris_logement_familles', 
    'paris_logement_aspeh', 'paris_logement_plfm', 'paris_logement_psol',
    'parisien']
  for key in paris_keys:
    json_content = delete_key(json_content, 'familles/_/' + key)
  
  transport_keys = ['brest_metropole_transport', 'rennes_metropole_transport']
  for key in transport_keys:
    json_content = delete_key(json_content, 'individus/demandeur/' + key)
    json_content = delete_key(json_content, 'individus/enfant_0/' + key)

  json_content = delete_mesaides_pre_computed_keys(json_content, '2018-01')


def delete_mesaides_pre_computed_keys(json_content, period_str):
  json_content = delete_key(json_content, 'familles/_/acs/' + period_str)
  json_content = delete_key(json_content, 'familles/_/af/' + period_str)
  json_content = delete_key(json_content, 'familles/_/aide_logement/' + period_str)
  json_content = delete_key(json_content, 'familles/_/aide_logement_non_calculable/' + period_str)
  json_content = delete_key(json_content, 'familles/_/asf/' + period_str)
  json_content = delete_key(json_content, 'familles/_/asi/' + period_str)
  json_content = delete_key(json_content, 'familles/_/aspa/' + period_str)
  json_content = delete_key(json_content, 'familles/_/ass/' + period_str)
  json_content = delete_key(json_content, 'familles/_/bourse_college/' + period_str)
  json_content = delete_key(json_content, 'familles/_/bourse_lycee/' + period_str)
  json_content = delete_key(json_content, 'familles/_/cf/' + period_str)
  json_content = delete_key(json_content, 'familles/_/cmu_c/' + period_str)
  json_content = delete_key(json_content, 'familles/_/paje_base/' + period_str)
  json_content = delete_key(json_content, 'familles/_/ppa/' + period_str)
  json_content = delete_key(json_content, 'familles/_/rsa/' + period_str)
  json_content = delete_key(json_content, 'familles/_/rsa_non_calculable/' + period_str)
  json_content = delete_key(json_content, 'individus/demandeur/aah/' + period_str)
  json_content = delete_key(json_content, 'individus/demandeur/aah_non_calculable/' + period_str)
  json_content = delete_key(json_content, 'individus/demandeur/acs/' + period_str)  # TODO Check existence.


if __name__ == "__main__":
  try:
    json_target = sys.argv[1]

    if os.path.isdir(json_target):
      for file in os.listdir(json_target):
        if is_json(file):
          log.debug("> " + file)
          update_json(os.path.join(json_target, file), from_mesaides_to_openfisca)  
    else:
      if not is_json(json_target):
        log.error(u"")
      update_json(json_target, from_mesaides_to_openfisca)

  except BaseException as e:
    if len(sys.argv) == 1:
      log.error(u"Missing a directory or a .json file to clean.")
      log.warn(u"USAGE : python clean_mes_aides_situation.py target")
      log.warn(u"        where 'target' is a directory containing .json file OR one .json file to clean.")
    else:
      if e.message:
        log.error(str(e.__class__.__name__)+ ': ' + e.message)
      else:
        log.error(e)

