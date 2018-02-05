# -*- coding: utf-8 -*-

####### Importez OpenFisca  ###########

import openfisca_france
from openfisca_core.simulations import Simulation
import json
import csv


from clean_mes_aides_situations import normalize

####### Listez les entités ###########

situations_json = [
    #'situations/celib_smic_aucune_aides.json',
    #'situations/couple_retraites.json'
    '/repos/tutorial/python/exemples/gt_non_recours/celibataire_aah_mes-aides_5a70bfe34b64656dc14d58a5'
]

####### Listez les calculs à effectuer et les periodes sur lequels les calculer ###########


jan18 = '2018-01'


toremove = {
    'familles': {
        'acs': jan18,
        'af': jan18,
        'aide_logement': jan18,
        'aide_logement_non_calculable': jan18,
        'asf': jan18,
        'asi': jan18,
        'aspa': jan18,
        'ass': jan18,
        'bourse_college': jan18,
        'bourse_lycee': jan18,
        'cf': jan18,
        'cmu_c': jan18,
        'paje_base': jan18,
        'ppa': jan18,
        'rsa': jan18,
        'rsa_non_calculable': jan18
        },
    'individus': {
        'aah': jan18,
        'aah_non_calculable': jan18,
        'acs': jan18,
        'acs': jan18,
        'acs': jan18
    }
}

def removeComputedValues(situation):
    for entityKey in toremove:
        entities = situation[entityKey]
        props = toremove[entityKey]

        for instanceKey in entities:
            entity = entities[instanceKey]

            for prop in props:
                if prop in entity:
                    del entity[prop]

    return situation

year17 = '2017'
periods = [jan18]

calculs = {
    'rfr': [year17],
    'aah_base_ressources': periods,
    'ass_base_ressources': periods,
    'cmu_base_ressources': periods,
    'prestations_familiales_base_ressources': periods,
    'rsa':  periods,
    'aide_logement': periods
}




fieldnames = ['Situation']

for calcul, periods in calculs.iteritems():
    for period in periods:
        label = calcul + '<' + period + '>'
        fieldnames.append(label)

##### Initialiser le fichier CSV pour export Excel ######

with open('resultats.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for situation_json in situations_json:
        with open(situation_json) as json_data:
            json_str = json_data.read()
            situation = json.loads(json_str)

        results = {"Situation": situation_json}

        ####### Initialisez la simulation (rencontre des entités avec la legislation) ##############

        legislation_france = openfisca_france.FranceTaxBenefitSystem()
        simulation_actuelle = Simulation(tax_benefit_system=legislation_france, simulation_json=removeComputedValues(normalize(situation)))

        ##### Demandez l'ensemble des calculs #####
        for calcul, periods in calculs.iteritems():
            for period in periods:
                label = calcul + '<' + period + '>'
                results[label] = simulation_actuelle.calculate(calcul, period)[0]

        ##### Ecrire les resultats dans le CSV
        writer.writerow(results)

print 'le calcul est terminé'
