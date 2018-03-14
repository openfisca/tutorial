# -*- coding: utf-8 -*-
from openfisca_core import reforms
from openfisca_core import periods
from openfisca_france.model.base import *
from numpy import logical_or as or_

class af_eligibilite_base(Variable):
    value_type = bool
    entity = Famille
    label = u"Allocations familiales - Éligibilité pour la France métropolitaine sous condition de ressources"
    definition_period = MONTH

    def formula(famille, period):
        residence_dom = famille.demandeur.menage('residence_dom', period)
        af_nbenf = famille('af_nbenf', period)

        return not_(residence_dom) * (af_nbenf >= 1)

class af_base(Variable):
    value_type = float
    entity = Famille
    label = u"Allocations familiales - allocation de base"
    definition_period = MONTH
    # prestations familiales (brutes de crds)

    def formula(famille, period, parameters):
        eligibilite_base = famille('af_eligibilite_base', period)
        eligibilite_dom = famille('af_eligibilite_dom', period)
        af_nbenf = famille('af_nbenf', period)

        pfam = parameters(period).prestations.prestations_familiales.af

        eligibilite = or_(eligibilite_base, eligibilite_dom)

        #un_seul_enfant = eligibilite_dom * (af_nbenf == 1) * pfam.af_dom.taux_enfant_seul
        deux_enfants = (af_nbenf >= 1) * pfam.taux.enf2
        plus_de_trois_enfants = max_(af_nbenf - 2, 0) * pfam.taux.enf3
        taux_total = deux_enfants + plus_de_trois_enfants
        #deux_enfants égal un_seul_enfant dans le contexte de cette réforme
        montant_base = eligibilite * round_(pfam.bmaf * taux_total, 2)
        coeff_garde_alternee = famille('af_coeff_garde_alternee', period)
        montant_base = montant_base * coeff_garde_alternee

        af_taux_modulation = famille('af_taux_modulation', period)
        montant_base_module = montant_base * af_taux_modulation

        return montant_base_module

# Cette partie rassemble les changements dans une seule réforme appelée ici MaReforme
class reforme_1enfant(reforms.Reform):

    def apply(self):
        self.update_variable(af_base)
        self.update_variable(af_eligibilite_base)
