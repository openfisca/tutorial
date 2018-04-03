# -*- coding: utf-8 -*-

####### Importez OpenFisca  ###########

import openfisca_france
from openfisca_core.simulations import Simulation
from reforme_structurelle import MaReform
import json


####### Décrivez les entités ###########

json_path='situations/couple_2-enfants_revenus-2303-mois.json'

with open(json_path) as json_data:
    json1_str = json_data.read()
    situation = json.loads(json1_str)

####### Calculez la situation actuelle de la legislation française ##############

legislation_france = openfisca_france.FranceTaxBenefitSystem()
simulation_actuelle = Simulation(tax_benefit_system=legislation_france, simulation_json=situation)

# Insérez ci-dessous la variable que vous souhaitez calculer (ex : 'aah_base_ressources')
# ainsi que la periode sur laquelle vous souaitez la calculer (ex : '2017')

bases_ressources = ['aah_base_ressources', 'ass_base_ressources', 'cmu_base_ressources', 'prestations_familiales_base_ressources']

for base in bases_ressources:
    print (base)
    print (simulation_actuelle.calculate(base, '2018-01'))
    print ('---')


# ####### Calcule la situation avec la réforme ##############
print('#### Réforme ####')
legislation_reforme = MaReform(legislation_france)
simulation_reforme = Simulation(tax_benefit_system=legislation_reforme, simulation_json=situation)

# Insérez ci-dessous la variable que vous souhaitez calculer (ex : 'impots_directs')
# ainsi que la periode sur laquelle vous souhaitez la calculer (ex : '2017')
bases_ressources = [ 'base_ressource_mensuelle_individu', ]

for base in bases_ressources:
    print (base)
    print (simulation_reforme.calculate(base, '2018-01'))
    print ('---')
