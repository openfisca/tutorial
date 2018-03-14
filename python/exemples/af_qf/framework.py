# -*- coding: utf-8 -*-
####### Importez OpenFisca  ###########

import openfisca_france
from framework_methods import *
from reformes.reforme_test import MaReform

legislation_france = openfisca_france.FranceTaxBenefitSystem()

reformes = {
    "Reforme de test" : MaReform(legislation_france)
}

####### Listez les entités ###########

situations = "situations/"

####### Listez les calculs à effectuer et les périodes sur lequelles les calculer ###########

period_month = '2018-03'
period_year = '2017'
calculs = {
    'af_eligibilite_base': period_month,
    'af_base': period_month,
    'af': period_month,
}


run_framework(reformes, situations, calculs)


