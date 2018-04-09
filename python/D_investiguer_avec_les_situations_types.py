# -*- coding: utf-8 -*-

####### Importez OpenFisca  ###########

import openfisca_france
from openfisca_core.simulations import Simulation
import json
import csv


####### Listez les entités ###########

situations_json = [
    'situations/celib_smic_aucune_aides.json',
    'situations/couple_retraites.json'
]

####### Listez les calculs à effectuer et les periodes sur lequels les calculer ###########

calculs = {
    'rfr': '2017',
    'aah_base_ressources': '2018-01',
    'ass_base_ressources': '2018-01',
    'cmu_base_ressources': '2018-01',
    'prestations_familiales_base_ressources': '2018-01'
}

##### Initialiser le fichier CSV pour export Excel ######

with open('resultats.csv', 'w') as csvfile:
    fieldnames = ['Situation'] + list(calculs)
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for situation_json in situations_json:
        with open(situation_json) as json_data:
            json_str = json_data.read()
            situation = json.loads(json_str)

        results = {"Situation": situation_json}

        ####### Initialisez la simulation (rencontre des entités avec la legislation) ##############

        legislation_france = openfisca_france.FranceTaxBenefitSystem()
        simulation_actuelle = Simulation(tax_benefit_system=legislation_france, simulation_json=situation)

        ##### Demandez l'ensemble des calculs #####
        for calcul, period in calculs.iteritems():
            results[calcul] = simulation_actuelle.calculate(calcul, period)[0]

        ##### Ecrire les resultats dans le CSV
        writer.writerow(results)

print ('le calcul est terminé')
