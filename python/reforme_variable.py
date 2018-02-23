# -*- coding: utf-8 -*-
from openfisca_core import reforms
from openfisca_france.model.base import *

####### Décrivez votre réforme ###########

# Cette partie décrit les changements
class base_ressource_mensuelle_individu(Variable):
    value_type = float
    entity = Individu
    label = u"Base de ressource mensuelle d'un individu"
    definition_period = MONTH
    reference = u"???"

    def formula(individu, period, parameters):
        salaires = individu('salaire_net_hors_revenus_exceptionnels', period)
        primes_salaires_net = individu('primes_salaires_net', period)


        return (
                salaires +
                primes_salaires_net
        )

# Cette partie rassemble les changements dans une seule réforme appelée ici MaReforme
class MaReform(reforms.Reform):
    def apply(self):
        self.add_variable(base_ressource_mensuelle_individu)
