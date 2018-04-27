import openfisca_france
from openfisca_france.model.base import *
from openfisca_core import reforms

class aide_logement_base_ressources_initiale(Variable):
    value_type = float
    entity = Famille
    label = u"Base ressources des allocations logement"
    definition_period = MONTH

    def formula(famille, period, parameters):
        size_in_months = 1
        ressource_period = period.start.period('month', size_in_months).offset(-size_in_months)
        salaire_imposable_individus = famille.members('salaire_net', ressource_period, options = [ADD])
        salaire_imposable = famille.sum(salaire_imposable_individus)

        annual_scaling = 12 / size_in_months
        return salaire_imposable * 0.9 * annual_scaling

class reforme(reforms.Reform):

    def apply(self):
        self.update_variable(aide_logement_base_ressources_initiale)