# -*- coding: utf-8 -*-
####### Importez OpenFisca  ###########

import openfisca_france
from framework_methods import *
from reformes.reforme_test import MaReform

legislation_france = openfisca_france.FranceTaxBenefitSystem()

reformes = {
    "France" : legislation_france,  # situation actuelle
    "Reforme de test" : MaReform(legislation_france)
}

####### Listez les entités ###########

situations = "situations_test/"

####### Listez les calculs à effectuer et les périodes sur lequelles les calculer ###########

period_month = '2018-02'
period_year = '2017'
calculs = {
    # 'base_ressource_mensuelle_individu': period_month,
    # 'base_ressource_mensuelle_famille': period_month,
    # 'base_ressource_annuelle_individu': period_year,
    # 'base_ressources_al_2019': period_month,
    'aide_logement_base_ressources': period_month
}


run_framework(reformes, situations, calculs)


