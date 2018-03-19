# -*- coding: utf-8 -*-
from openfisca_core import reforms
from openfisca_core import periods
from openfisca_france.model.base import *
from numpy import logical_or as or_

class af(Variable):
    calculate_output = calculate_output_add
    value_type = float
    entity = Famille
    label = u"Allocations familiales - total des allocations"
    definition_period = MONTH
    set_input = set_input_divide_by_period

    def formula_2015_07_01(famille, period, parameters):
        af_base = famille('af_base', period)
        af_majoration = famille('af_majoration', period)
        af_allocation_forfaitaire = famille('af_allocation_forfaitaire', period)
        af_complement_degressif = famille('af_complement_degressif', period)
        af_forfaitaire_complement_degressif = famille('af_allocation_forfaitaire_complement_degressif', period)

        return (
            (af_base + af_majoration + af_allocation_forfaitaire + af_complement_degressif +
            af_forfaitaire_complement_degressif) * 2
)
        
# Cette partie rassemble les changements dans une seule réforme appelée ici MaReforme
class double_af(reforms.Reform):

    def apply(self):
        self.update_variable(af)
        
