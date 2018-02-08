# -*- coding: utf-8 -*-
from openfisca_core import reforms
from openfisca_core import periods
from openfisca_france.model.base import *


class base_ressource_mensuelle_individu(Variable):
    value_type = float
    entity = Individu
    label = u"Base de ressource mensuelle d'un individu"
    definition_period = MONTH
    reference = u"???"

    def formula(individu, period, parameters):
        salaires = individu('salaire_net_hors_revenus_exceptionnels', period)


        return salaires

# Cette partie rassemble les changements dans une seule réforme appelée ici MaReforme
class MaReform(reforms.Reform):

    def apply(self):
        self.add_variable(base_ressource_mensuelle_individu)

