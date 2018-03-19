# -*- coding: utf-8 -*-
from openfisca_core import reforms
from openfisca_core import periods
from openfisca_france.model.base import *
from numpy import logical_or as or_

class af_taux_modulation(Variable):
    value_type = float
    default_value = 1
    entity = Famille
    label = u"Taux de modulation à appliquer au montant des AF depuis 2015"
    definition_period = MONTH

    def formula_2015_07_01(famille, period, parameters):
        af_nbenf = famille('af_nbenf', period)
        pfam = parameters(period).prestations.prestations_familiales.af
        base_ressources = famille('prestations_familiales_base_ressources', period)
        modulation = pfam.modulation
        plafond0 = 20989 + (af_nbenf>=2)*3143
        plafond1 = modulation.plafond_tranche_1 + max_(af_nbenf - 2, 0) * modulation.majoration_plafond_par_enfant_supplementaire
        plafond2 = modulation.plafond_tranche_2 + max_(af_nbenf - 2, 0) * modulation.majoration_plafond_par_enfant_supplementaire
        taux_tranche_0 = 1.25

        taux = (
            (base_ressources <= plafond0) * taux_tranche_0 +
            (base_ressources > plafond0) * (base_ressources <= plafond1) * 1 +
            (base_ressources > plafond1) * (base_ressources <= plafond2) * modulation.taux_tranche_2 +
            (base_ressources > plafond2) * modulation.taux_tranche_3
        )

        return taux
    
# Cette partie rassemble les changements dans une seule réforme appelée ici MaReforme
class reforme_tranche0(reforms.Reform):

    def apply(self):
        self.update_variable(af_taux_modulation)