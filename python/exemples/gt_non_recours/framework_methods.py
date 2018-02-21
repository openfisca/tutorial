# -*- coding: utf-8 -*-
import json
import csv
import os
from openfisca_core.simulations import Simulation, SituationParsingError
from openfisca_core.parameters import ParameterNotFound


def removeComputedValues(situation):
    toremove = {
        'familles': {
            'acs': '2018-01',
            'af': '2018-01',
            'aide_logement': '2018-01',
            'aide_logement_non_calculable': '2018-01',
            'asf': '2018-01',
            'asi': '2018-01',
            'aspa': '2018-01',
            'ass': '2018-01',
            'bourse_college': '2018-01',
            'bourse_lycee': '2018-01',
            'cf': '2018-01',
            'cmu_c': '2018-01',
            'paje_base': '2018-01',
            'ppa': '2018-01',
            'rsa': '2018-01',
            'rsa_non_calculable': '2018-01'
        },
        'individus': {
            'aah': '2018-01',
            'aah_non_calculable': '2018-01',
            'acs': '2018-01',
            'acs': '2018-01',
            'acs': '2018-01'
        }
    }

    for entityKey in toremove:
        entities_in_situ = situation[entityKey] # Familles
        variables = toremove[entityKey] # {acs : jan-01, ...}

        for entity_id in entities_in_situ:
            entity_in_situ = entities_in_situ[entity_id]

            for variable in variables: # acs
                if variable in entity_in_situ:
                    del entity_in_situ[variable]

    return situation


def run_situation(reform_name, reform, situation_json,  calculs):
    with open(situation_json) as json_data:
        json_str = json_data.read()
        situation = json.loads(json_str)

    results = {"Situation": situation_json, "Legislation": reform_name}

    ####### Initialisez la simulation (rencontre des entités avec la legislation) ##############

    simulation = Simulation(tax_benefit_system=reform, simulation_json=removeComputedValues(situation))

    ##### Demandez l'ensemble des calculs #####
    for calcul, period in calculs.iteritems():
        results
        try:
            results[calcul] = simulation.calculate(calcul, period)[0]
            print('. ' + calcul)
        except ParameterNotFound as e:
            print 'x ' + calcul
            print e.message + os.linesep

    return results

def run_reform(reform_name, reform, situations_directory, calculs):
    print '# ' + reform_name
    calculs_situation_reform = []

    situations_json = []
    for situation in os.listdir(situations_directory):
        if situation.endswith('.json'):
            situations_json.append(os.path.join(situations_directory, situation))

    for situation_json in situations_json:
        try:
            calculs_situation = run_situation(reform_name, reform, situation_json, calculs)
            calculs_situation_reform.append(calculs_situation)
            print('/ ' + situation_json)
        except SituationParsingError as e:
            print 'situation mal formée : ' + situation_json
            print str(e.message) + os.linesep
    return calculs_situation_reform


def run_framework(reforms, situations, computations):
    resultats = []

    for reform in reforms:
        resultats += run_reform(reform, reforms[reform], situations, computations)

    ##### Initialiser le fichier CSV pour export Excel ######

    with open('resultats.csv', 'w') as csvfile:
        fieldnames = ['Legislation', 'Situation'] + list(computations)
        # Situation, Variable, Period, Value
        # rfr, rsa, aah
        # rfr, 2016
        # rsa, 2018
        # aah, 2018
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for result in resultats:
            writer.writerow(result)

    print 'le calcul est terminé'




