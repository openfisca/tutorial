# -*- coding: utf-8 -*-
import json
import csv
import os
from openfisca_core.simulations import Simulation


def run_situation(reform_name, reform, situation_json,  calculs):
    with open(situation_json) as json_data:
        json_str = json_data.read()
        situation = json.loads(json_str)

    results = {"Situation": situation_json, "Legislation": reform_name}

    ####### Initialisez la simulation (rencontre des entités avec la legislation) ##############

    simulation = Simulation(tax_benefit_system=reform, simulation_json=situation)

    ##### Demandez l'ensemble des calculs #####
    for calcul, period in calculs.iteritems():
        results
        results[calcul] = simulation.calculate(calcul, period)[0]
        print('.')

    return results

def run_reform(reform_name, reform, situations_directory, calculs):
    print '#'
    calculs_situation_reform = []

    situations_json = []
    for situation in os.listdir(situations_directory):
        situations_json.append(os.path.join(situations_directory, situation))



    for situation_json in situations_json:
        calculs_situation = run_situation(reform_name, reform, situation_json, calculs)
        calculs_situation_reform.append(calculs_situation)
        print('/')
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

