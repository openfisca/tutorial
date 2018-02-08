# -*- coding: utf-8 -*-
####### Importez OpenFisca  ###########

import openfisca_france
from framework_methods import *
from reformes.reforme_test import MaReform

legislation_france = openfisca_france.FranceTaxBenefitSystem()

reformes = {
    #"France" : legislation_france,
    "Reforme de test" : MaReform(legislation_france)
}

####### Listez les entités ###########

situations = "situations_test/"

####### Listez les calculs à effectuer et les periodes sur lequels les calculer ###########

period_month = '2018-02'
period_year = '2017'
calculs = {
    'BMGG': period_month,
}


run_framework(reformes, situations, calculs)


