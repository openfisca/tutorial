# -*- coding: utf-8 -*-

####### Importez OpenFisca  ###########

import openfisca_france
from openfisca_core.simulations import Simulation
from openfisca_core import reforms
from openfisca_core import periods
import json

####### Décrivez votre réforme ###########

# Cette partie décrit les changements
def modify_my_parameters(parameters):
    reform_year = 2018
    reform_period = periods.period(reform_year)
    parameters.impot_revenu.bareme[1].rate.update(start=reform_period, value=0)
    return parameters

# Cette partie rassemble les changements dans une seule réforme appelée ici MaReforme
class MaReform(reforms.Reform):
    def apply(self):
        self.modify_parameters(modifier_function = modify_my_parameters)


####### Décrivez les entités ###########

with open('situations/couple_retraites.json') as json_data:
    json1_str = json_data.read()
    situation = json.loads(json1_str)

####### Calculez la situation actuelle de la legislation française ##############

legislation_france = openfisca_france.FranceTaxBenefitSystem()
simulation_actuelle = Simulation(tax_benefit_system=legislation_france, simulation_json=situation)

# Insérez ci-dessous la variable que vous souhaitez calculer (ex : 'impots_directs')
# ainsi que la periode sur laquelle vous souaitez la calculer (ex : '2017')
print('base_ressources_apa n-2')
resultat_actuel = simulation_actuelle.calculate('base_ressources_apa', '2017-01')
resultat_actuel = simulation_actuelle.calculate('rfr', '2017')

print "Résultat actuel"
print resultat_actuel

####### Calcule la situation avec la réforme ##############
legislation_reforme = MaReform(legislation_france)
simulation_reforme = Simulation(tax_benefit_system=legislation_reforme, simulation_json=situation)

# Insérez ci-dessous la variable que vous souhaitez calculer (ex : 'impots_directs')
# ainsi que la periode sur laquelle vous souaitez la calculer (ex : '2017')
resultat_reforme = simulation_reforme.calculate('base_ressources_apa', '2017-01')
resultat_reforme = simulation_reforme.calculate('rfr', '2017')

print "Resultat après reforme"
print resultat_reforme


# base_ressources_apa / mois
# rsa_base_ressources / mois
# aah_base_ressources / mois
# ass_base_ressources / mois
# cmu_base_ressources / mois
# ppa_base_ressources / mois
# asi_aspa_base_ressources / mois
# rsa_base_ressources / mois
# prestations_familiales_base_ressources / mois


