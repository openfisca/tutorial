# -*- coding: utf-8 -*-

####### Importez OpenFisca  ###########


import openfisca_france
from openfisca_core.simulations import Simulation
from openfisca_france.model.base import *
from openfisca_core import reforms
import json
import csv

####### Listez les entités ###########

# -*- coding: utf-8 -*-

from os import listdir
from os.path import isfile, join
from pprint import pprint


legislation_france = openfisca_france.FranceTaxBenefitSystem()

# Cette partie rassemble les changements dans une seule réforme appelée ici MaReforme


class aide_logement_base_ressources_initiale(Variable):
    value_type = float
    entity = Famille
    label = u"Base ressources des allocations logement"
    definition_period = MONTH

    def formula(famille, period, parameters):
        periods = [period] # monthly periods
        salaire_imposable_individus = famille.members('salaire_imposable', periods, options = [ADD])
        salaire_imposable = famille.sum(salaire_imposable_individus)

        annual_scaling = 12 / len(periods)
        return salaire_imposable * 0.9 * annual_scaling


class AL_MM1(reforms.Reform):

    def apply(self):
        self.update_variable(aide_logement_base_ressources_initiale)

al_reforms = [{'name':'Base', 'legislation': 'l2'}, { 'name': 'AL_MM1', 'legislation': 'l1' }]

al_reforms = [{'name':'Base', 'legislation': legislation_france}, { 'name': 'AL_MM1', 'legislation': AL_MM1(legislation_france) }]


stable = {
    'familles': {
        'f1': {
            'parents': ['Faustine']
        }
    },
    'foyers_fiscaux': {
        'ff1': {
            'declarants': ['Faustine']
        }
    },
    'individus': {
        'Faustine': {
            'salaire_imposable': {
                '2015': 12 * 700,
                '2016': 12 * 700,
                '2017': 12 * 700,
                '2018': 12 * 700,
                '2019': 12 * 700
            }
        }
    },
    'menages': {
        'm1': {
            'personne_de_reference': ['Faustine'],
            'loyer': {
                '2015': 12 * 500,
                '2016': 12 * 500,
                '2017': 12 * 500,
                '2018': 12 * 500,
                '2019': 12 * 500
            },
            'statut_occupation_logement': {
                '2015': 'locataire_vide',
                '2016': 'locataire_vide',
                '2017': 'locataire_vide',
                '2018': 'locataire_vide',
                '2019': 'locataire_vide'
            }
        }
    }
}
years = [str(y).zfill(2) for y in range(2015, 2020)]
monthIds = [ str(m).zfill(2) for m in range(1,13) ]
allMonths = [y + '-' + m for y in years for m in monthIds]
months2018 = [ '2018-' + m for m in monthIds ]
months2019 = [ '2019-' + m for m in monthIds ]
year17 = '2017'
periods = months2018

calculs = {
    'prestations_familiales_base_ressources_individu': allMonths,
    'aide_logement': periods,
    'aide_logement_base_ressources': periods,
    'rsa_base_ressources_statique': periods,
    'traitements_salaires_pensions_rentes': years,
    'aide_logement_base_ressources_defaut': allMonths,
    'aide_logement_base_ressources_eval_forfaitaire': allMonths,
    'revenu_assimile_salaire_apres_abattements': years,
    'abattement_salaires_pensions': years
}

fieldnames = ['Situation', 'Reform', 'Period', 'Variable', 'Value']

with open('resultats.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    results = {'Situation': 'stable'}

    ####### Initialisez la simulation (rencontre des entités avec la legislation) ##############

    for reform in al_reforms:

        results['Reform'] = reform['name']
        simulation_actuelle = Simulation(tax_benefit_system=reform['legislation'], simulation_json=stable)

        ##### Demandez l'ensemble des calculs #####
        for calcul, periods in calculs.iteritems():
            results['Variable'] = calcul
            for period in periods:
                results['Period'] = period
                data = simulation_actuelle.calculate(calcul, period)
                pprint(data)
                results['Value'] = data[0]
                writer.writerow(results)

print 'le calcul est terminé'

# # -*- coding: utf-8 -*-
# ####### Importez OpenFisca  ###########

# import openfisca_france
# from framework_methods import *
# from reformes.reforme_test import MaReform

# legislation_france = openfisca_france.FranceTaxBenefitSystem()

# reformes = {
#     "France" : legislation_france,  # situation actuelle
#     "Reforme de test" : MaReform(legislation_france)
# }

# ####### Listez les entités ###########

# situations = "situations_test/"

# ####### Listez les calculs à effectuer et les périodes sur lequelles les calculer ###########

# period_month = '2018-02'
# period_year = '2017'
# calculs = {
#     # 'base_ressource_mensuelle_individu': period_month,
#     # 'base_ressource_mensuelle_famille': period_month,
#     # 'base_ressource_annuelle_individu': period_year,
#     # 'base_ressources_al_2019': period_month,
#     'aide_logement_base_ressources': period_month,
#     'aide_logement': period_month,
#     'loyer': period_month
# }


# run_framework(reformes, situations, calculs)


