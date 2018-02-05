# -*- coding: utf-8 -*-
####### Importez OpenFisca  ###########

import openfisca_france
from framework_methods import *
from reformes.reforme_test import MaReform
import os

legislation_france = openfisca_france.FranceTaxBenefitSystem()

reformes = {
    "France" : legislation_france,
    "Reforme de test" : MaReform(legislation_france)}

####### Listez les entités ###########

situations = "situations/"

####### Listez les calculs à effectuer et les periodes sur lequels les calculer ###########

calculs = {
    'rfr': '2017',
    'aah_base_ressources': '2018-02',
    'ass_base_ressources': '2018-02',
    'cmu_base_ressources': '2018-02',
    'prestations_familiales_base_ressources': '2018-02',
    'prestations_familiales_base_ressources_individu' : '2018-02'
}


run_framework(reformes, situations, calculs)


