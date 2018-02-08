# -*- coding: utf-8 -*-
from openfisca_core import reforms
from openfisca_core import periods
from openfisca_france.model.base import *

class BMGG(Variable):
    value_type = float
    entity = Individu
    label = u"Base de ressource mensuelle d'un individu"
    definition_period = MONTH
    reference = u"???"

    def formula(individu, period, parameters):
        salaires = individu(salaire_net_hors_revenus_exceptionnels, period)


        return salaires



class aide_logement_abattement_depart_retraite(Variable):
    value_type = float
    entity = Individu
    label = u"Montant de l'abattement sur les salaires en cas de départ en retraite"
    definition_period = MONTH
    # Article R532-5 du Code de la sécurité sociale
    reference = u"https://www.legifrance.gouv.fr/affichCodeArticle.do?idArticle=LEGIARTI000006750910&cidTexte=LEGITEXT000006073189&dateTexte=20151231"

    def formula(individu, period, parameters):
        m_13 = period.offset(-13, 'month')
        retraite_m_13 = individu('retraite_imposable', m_13, options = [ADD])
        activite = individu('activite', period)
        retraite = activite == TypesActivite.retraite
        condition_abattement = (retraite_m_13 == 0) * retraite

        # [from period.m_13 to period.m_1]
        m_13_to_m_1 = m_13.start.period('year', 1)
        revenus_activite_pro = individu('revenu_assimile_salaire_apres_abattements', m_13_to_m_1)
        revenus_du_chomage = individu('revenu_du_chomage', m_13_to_m_1)
        abattement = condition_abattement * 0.3 * (revenus_activite_pro + revenus_du_chomage)

        return abattement


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
