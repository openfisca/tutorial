# -*- coding: utf-8 -*-
####### Importez OpenFisca  ###########

import openfisca_france
from framework_methods import *
from reformes.reforme_1er_enfant import reforme_1enfant
from reformes.increase_bmaf import increase_bmaf
from reformes.reforme_tranche0 import reforme_tranche0
from reformes.delete_plafond_qf import delete_plafond_qf
from reformes.double_af import double_af
legislation_france = openfisca_france.FranceTaxBenefitSystem()

reformes = {
    "Legislation actuelle" : legislation_france, 
    "Reforme 1er enfant" : reforme_1enfant(legislation_france),
    "Reforme BMAF" : increase_bmaf(legislation_france),
    "Reforme Tranche 0" : reforme_tranche0(legislation_france),
    "Reforme Plafond QF" : delete_plafond_qf(legislation_france),
    "Reforme AF double" : double_af(legislation_france),
    "Reforme cumulee 1" : reforme_1enfant(reforme_tranche0((increase_bmaf(legislation_france)))),
    "Reforme cumulee 2" : reforme_1enfant(reforme_tranche0((double_af(legislation_france))))
}

####### Listez les entités ###########

situations = "situations/"

####### Listez les calculs à effectuer et les périodes sur lequelles les calculer ###########

period_month = '2018-03'
period_year = '2018'
calculs = {
    'af_eligibilite_base': period_month,
    'af_base': period_month,
    'af': period_month,
    'ir_plaf_qf' : 2017,
    'ir_ss_qf': "2017",
    'ir_brut': "2017",
    'irpp':2017
}


run_framework(reformes, situations, calculs)


