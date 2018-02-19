# -*- coding: utf-8 -*-
from openfisca_core import reforms
from openfisca_core import periods
from openfisca_france.model.base import *

# Question : 'indemnites_journalieres_imposables' semble dire que certaines indemnités journalières ne sont imposables qu'à 50%, doit on prendre 50% de ces montants ?
# question : indemnites_journalieres_maladie_professionnelle ne tourne pas et on ne sait pas pourquoi

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
        # complement_allocation_adulte_handicape = individu('caah', period)
        majoration_vie_autonome = individu('mva', period)
        prestation_compensation_handicap = individu('pch', period)

        indemnites_journalieres_maternite = individu('indemnites_journalieres_maternite', period)
        indemnites_journalieres_maladie = individu('indemnites_journalieres_maladie', period)
        # indemnites_journalieres_maladie_professionnelle = individu('indemnites_journalieres_maladie_professionnelle, period)', period)
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

        return (
                salaires +
                primes_salaires_net +
                indemnites_stage +
                revenus_stage_formation_pro +
                chomage_net +
                allocation_securisation_professionnelle +
                prime_forfaitaire_mensuelle_reprise_activite +
                allocation_adulte_handicape +
                # complement_allocation_adulte_handicape +
                majoration_vie_autonome +
                prestation_compensation_handicap +
                indemnites_journalieres_maternite +
                indemnites_journalieres_maladie +
                # indemnites_journalieres_maladie_professionnelle +
                indemnites_journalieres_accident_travail +
                indemnites_chomage_partiel +
                indemnites_volontariat +
                indemnite_fin_contrat_net +
                dedommagement_victime_amiante +
                pensions_alimentaires_percues +
                pensions_alimentaires_versees_individu +
                prestation_compensatoire +
                retraite_nette +
                retraite_combattant +
                pensions_invalidite +
                bourse_enseignement_sup +
                bourse_recherche +
                gains_exceptionnels +
                revenus_locatifs +
                revenus_capital +
                tns_auto_entrepreneur_chiffre_affaires
        )


class base_ressource_mensuelle_famille(Variable):
    value_type = float
    entity = Famille
    label = u"Base de ressource mensuelle d'une famille"
    definition_period = MONTH
    reference = u"???"

    def formula(famille, period, parameters):
        # aide_logement = famille('aide_logement', period)
        allocations_familiales = famille('af', period)
        complement_familial = famille('cf', period)
        allocation_soutien_familial = famille('asf', period)
        # revenu_solidarite_active = famille('rsa', period)
        # prime_activite = famille('ppa', period)

        allocation_solidarite_personnes_agees = famille('aspa', period)
        allocation_suplementaire_invalidite = famille('asi', period)
        allocation_solidarite_specifique = famille('ass', period)
        allocation_education_enfant_handicape = famille('aeeh', period)

        paje_base = famille('paje_base', period)
        paje_clca = famille('paje_clca', period)
        paje_prepare = famille('paje_prepare', period)
        
        base_ressources_membres = famille.sum(famille.members('base_ressource_mensuelle_individu', period))

        return (
            # aide_logement +
            allocations_familiales +
            complement_familial +
            allocation_soutien_familial +
            # revenu_solidarite_active +
            # prime_activite +
            allocation_solidarite_personnes_agees +
            allocation_suplementaire_invalidite +
            allocation_solidarite_specifique +
            allocation_education_enfant_handicape +
            paje_base +
            paje_clca +
            paje_prepare +
            base_ressources_membres
        )


class base_ressource_annuelle_individu(Variable):
    value_type = float
    entity = Individu
    label = u"Base de ressource annuelle d'un individu"
    definition_period = YEAR
    reference = u"???"

    def formula(individu, period, parameters):
        tns_micro_entreprise_chiffre_affaires = individu('tns_micro_entreprise_chiffre_affaires', period)
        tns_benefice_exploitant_agricole = individu('tns_benefice_exploitant_agricole', period)
        tns_autres_revenus = individu('tns_autres_revenus', period)

        return (
            tns_micro_entreprise_chiffre_affaires +
            tns_benefice_exploitant_agricole +
            tns_autres_revenus
        )


class aide_logement_base_ressources(Variable):
    value_type = float
    entity = Famille
    label = u"Base de ressource annuelle d'un individu"
    definition_period = MONTH
    reference = u"???"

    def formula(famille, period, parameters):
        annee = periods.instant(period).year
        annee_n = periods.instant(annee).period('year')
        annee_n1 = annee_n.offset(-1, 'year')

        base_ressource_annuelle_membres_famille = famille.sum(famille.members('base_ressource_annuelle_individu', annee_n1))
        # base_ressource_mensuelle_famille_n1 = famille.sum(
        #     famille('base_ressource_mensuelle_famille', annee_n1, options = [ADD])
        #     )

        return (
             # famille('base_ressource_mensuelle_famille', period.offset(-1, 'month'))
             + famille('base_ressource_mensuelle_famille', period.offset(-2, 'month'))
             + famille('base_ressource_mensuelle_famille', period.offset(-3, 'month'))
             + famille('base_ressource_mensuelle_famille', period.offset(-4, 'month'))
             + famille('base_ressource_mensuelle_famille', period.offset(-5, 'month'))
             + famille('base_ressource_mensuelle_famille', period.offset(-6, 'month'))
             + famille('base_ressource_mensuelle_famille', period.offset(-7, 'month'))
             + famille('base_ressource_mensuelle_famille', period.offset(-8, 'month'))
             + famille('base_ressource_mensuelle_famille', period.offset(-9, 'month'))
             + famille('base_ressource_mensuelle_famille', period.offset(-10, 'month'))
             + famille('base_ressource_mensuelle_famille', period.offset(-11, 'month'))
             + famille('base_ressource_mensuelle_famille', period.offset(-12, 'month'))
            + famille('base_ressource_mensuelle_famille', period.offset(-13, 'month'))
            # base_ressource_mensuelle_famille_n1
            + base_ressource_annuelle_membres_famille
        )

# Cette partie rassemble les changements dans une seule réforme appelée ici MaReforme
class MaReform(reforms.Reform):

    def apply(self):
        self.add_variable(base_ressource_mensuelle_individu)
        self.add_variable(base_ressource_mensuelle_famille)
        self.add_variable(base_ressource_annuelle_individu)
        self.update_variable(aide_logement_base_ressources)

