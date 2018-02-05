# -*- coding: utf-8 -*-
from openfisca_core import reforms
from openfisca_core import periods
from openfisca_france.model.base import *

# Cette partie décrit les changements
class prestations_familiales_base_ressources_individu(Variable):
        value_type = float
        is_period_size_independent = True
        entity = Individu
        label = u"Base ressource individuelle des prestations familiales"
        definition_period = MONTH

        def formula(individu, period):
            annee_fiscale_n_1 = periods.period('2017')

            traitements_salaires_pensions_rentes = individu('traitements_salaires_pensions_rentes', annee_fiscale_n_1)
            hsup = individu('hsup', annee_fiscale_n_1, options=[ADD])
            rpns = individu('rpns', annee_fiscale_n_1)
            glo = individu('glo', annee_fiscale_n_1)
            div = individu('div', annee_fiscale_n_1)

            return traitements_salaires_pensions_rentes + hsup + rpns + glo + div


# Cette partie rassemble les changements dans une seule réforme appelée ici MaReforme
class MaReform(reforms.Reform):
    def apply(self):
        self.update_variable(prestations_familiales_base_ressources_individu)
