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
        primes_salaires_net = individu('primes_salaires_net', period)
        indemnites_stage = individu('indemnites_stage', period)
        revenus_stage_formation_pro = individu('revenus_stage_formation_pro', period)
        chomage_net = individu('chomage_net', period)
        allocation_securisation_professionnelle = individu('allocation_securisation_professionnelle', period)
        prime_forfaitaire_mensuelle_reprise_activite = individu('prime_forfaitaire_mensuelle_reprise_activite', period)
        allocation_adulte_handicape = individu('aah', period)
        complement_allocation_adulte_handicape = individu('caah', period)
        majoration_vie_autonome = individu('mva', period)
        prestation_compensation_handicap = individu('pch', period)

        indemnites_journalieres_maternite = individu('indemnites_journalieres_maternite', period)
        indemnites_journalieres_maladie = individu('indemnites_journalieres_maladie', period)
        indemnites_journalieres_maladie_professionnelle, period) = individu('indemnites_journalieres_maladie_professionnelle, period)', period)
        indemnites_journalieres_accident_travail = individu('indemnites_journalieres_accident_travail', period)
        
        indemnites_chomage_partiel = individu('indemnites_chomage_partiel', period)
        indemnites_volontariat = individu('indemnites_volontariat', period)
        indemnite_fin_contrat_net = individu('indemnite_fin_contrat_net', period)
        
        dedommagement_victime_amiante = individu('dedommagement_victime_amiante', period)
        pensions_alimentaires_percues = individu('pensions_alimentaires_percues', period)
        pensions_alimentaires_versees_individu = individu('pensions_alimentaires_versees_individu', period)
        prestation_compensatoire = individu('prestation_compensatoire', period)
        retraite_nette = individu('retraite_nette', period)
        retraite_combattant = individu('retraite_combattant', period)
        pensions_invalidite = individu('pensions_invalidite', period)
        bourse_enseignement_sup = individu('bourse_enseignement_sup', period)
        bourse_recherche = individu('bourse_recherche', period)
        gains_exceptionnels = individu('gains_exceptionnels', period)
        revenus_locatifs = individu('revenus_locatifs', period)
        revenus_capital = individu('revenus_capital', period)
        tns_auto_entrepreneur_chiffre_affaires = individu('tns_auto_entrepreneur_chiffre_affaires', period)

        return salaires

class base_ressource_mensuelle_famille(Variable):
    value_type = float
    entity = Individu
    label = u"Base de ressource mensuelle d'une famille"
    definition_period = MONTH
    reference = u"???"

    def formula(individu, period, parameters):
        aide_logement = famille('aide_logement', period)
        allocations_familiales = famille('af', period)
        complement_familial = famille('cf', period)
        allocation_soutien_familial = famille('asf', period)
        revenu_solidarite_active = famille('rsa', period)
        prime_activite = famille('ppa', period)

        allocation_solidarite_personnes_agees = famille('aspa', period)
        allocation_suplementaire_invalidite = famille('asi', period)
        allocation_solidarite_specifique = famille('ass', period)
        allocation_education_enfant_handicape = famille('aeeh', period)

        paje_base = famille('paje_base', period)
        paje_clca = famille('paje_clca', period)
        paje_prepare = famille('paje_prepare', period)
        
        base_ressources_membres = famille.sum(famille.members('base_ressource_mensuelle_individu', period))

        return aide_logement


class base_ressource_annuelle_individu(Variable):
    value_type = float
    entity = Individu
    label = u"Base de ressource annuelle d'un individu"
    definition_period = MONTH
    reference = u"???"

    def formula(individu, period, parameters):
        tns_micro_entreprise_chiffre_affaires = individu('tns_micro_entreprise_chiffre_affaires', period)
        tns_benefice_exploitant_agricole = individu('tns_benefice_exploitant_agricole', period)
        tns_autres_revenus = individu('tns_autres_revenus', period)

        return tns_autres_revenus


# Cette partie rassemble les changements dans une seule réforme appelée ici MaReforme
class MaReform(reforms.Reform):

    def apply(self):
        self.add_variable(base_ressource_mensuelle_individu)

