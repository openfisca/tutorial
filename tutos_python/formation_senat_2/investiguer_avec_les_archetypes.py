# -*- coding: utf-8 -*-

####### Importez OpenFisca  ###########

import openfisca_france
from openfisca_core.simulations import Simulation
from openfisca_core import reforms
from openfisca_core import periods
import json


####### Décrivez les entités ###########

with open('situations/celib_smic_aucune_aides.json') as json_data:
    json1_str = json_data.read()
    situation = json.loads(json1_str)
    print(json_data.name)

####### Calculez la situation actuelle de la legislation française ##############

legislation_france = openfisca_france.FranceTaxBenefitSystem()
simulation_actuelle = Simulation(tax_benefit_system=legislation_france, simulation_json=situation)

# Insérez ci-dessous la variable que vous souhaitez calculer (ex : 'impots_directs')
# ainsi que la periode sur laquelle vous souaitez la calculer (ex : '2017')

print "Revenu Fiscal de Référence"
print simulation_actuelle.calculate('rfr', '2017')
print '---'

bases_ressources = ['aah_base_ressources', 'ass_base_ressources', 'cmu_base_ressources', 'prestations_familiales_base_ressources']

for base in bases_ressources:
    print base
    print simulation_actuelle.calculate(base, '2018-01')
    print '---'

