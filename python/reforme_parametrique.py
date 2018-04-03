# -*- coding: utf-8 -*-
from openfisca_core import reforms, periods
from openfisca_france.model.base import *

####### Décrivez votre réforme ###########

# Cette partie décrit les changements
def modifier_un_parametre(parameters):
    #Ceci décrit la periode sur laquelle va s'appliquer ce changement
    reform_year = 2017
    reform_period = periods.period(reform_year)
    #Cette partie propose un changement de taux pour le barème 1 (le second) de l'impot sur le revenu à partir du début de 2017.
    parameters.impot_revenu.bareme[1].rate.update(start=reform_period.start, value=0.145)
    return parameters

# Cette partie rassemble les changements de parametre dans une seule réforme appelée ici MaReforme
class MaReform(reforms.Reform):
    def apply(self):
        self.modify_parameters(modifier_function = modifier_un_parametre)
