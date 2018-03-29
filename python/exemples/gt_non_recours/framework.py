# -*- coding: utf-8 -*-

####### Importez OpenFisca  ###########

from openfisca_core.simulations import Simulation
import openfisca_france

import reformes
from periods import allMonths
from situations import situations

import csv

'''
    Générer un fichier CSV qui indique pour chaque contexte législatif choisi, 
    la valeur de chaque calcul défini pour une période et une liste de situations.
'''

####### Listez les contextes législatifs à évaluer (modèle courant, réformes) ###########

legislation_france = openfisca_france.FranceTaxBenefitSystem()

al_reforms = [
    {'name': 'Base', 'legislation': legislation_france},
    {'name': 'AL_MM01', 'legislation': reformes.reforme_al01M(legislation_france)},
    {'name': 'AL_MM03', 'legislation': reformes.reforme_al03M(legislation_france)},
    {'name': 'AL_MM12', 'legislation': reformes.reforme_al12M(legislation_france)},
]


####### Listez les calculs à effectuer et les periodes sur lequelles les calculer ###########

calculs = {
    'aide_logement_base_ressources': allMonths,
    'aide_logement': allMonths,
    'salaire_net': allMonths,
    'loyer': allMonths,
    # 'proportion_ressource_logement': allMonths,
    # 'taux_effort_logement': allMonths,
    'ppa': allMonths
}

fieldnames = ['Situation', 'Reform', 'Period', 'Variable', 'Value']

with open('resultats--.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for (name, situation) in situations.iteritems():
        results = {'Situation': name}

        for reform in al_reforms:
            ####### Initialisez la simulation (rencontre des situations avec la legislation) ##############
            simulation_actuelle = Simulation(
                tax_benefit_system=reform['legislation'],  # Législation actuelle ou législation réformée.
                simulation_json=situation)
            results['Reform'] = reform['name']

            ##### Demandez l'ensemble des calculs #####
            for calcul, periods in calculs.iteritems():
                results['Variable'] = calcul
                for period in periods:
                    results['Period'] = period
                    data = simulation_actuelle.calculate(calcul, period)
                    print(reform['name'] + ' - ' + calcul + ' - ' + str(data))
                    results['Value'] = data[0]
                    writer.writerow(results)

print 'le calcul est terminé'
