# -*- coding: utf-8 -*-

# Importez OpenFisca
import openfisca_france
from framework_methods import *
from reformes.reforme_test import MaReforme

legislation_france = openfisca_france.FranceTaxBenefitSystem()

reformes = {
    "Reforme de test" : MaReforme(legislation_france)
}

# Listez les entités
situations = "situations/"

# Listez les calculs à effectuer et les périodes sur lequelles les calculer
period_month = '2018-02'
period_year = '2017'
calculs = {
    'base_ressource_mensuelle_individu': period_month,
    'base_ressource_mensuelle_famille': period_month,
    'base_ressource_annuelle_individu': period_year,
    'aide_logement_base_ressources': period_month,
    'aide_logement': period_month,
    'loyer': period_month
}


run_framework(reformes, situations, calculs)
