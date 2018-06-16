# -*- coding: utf-8 -*-

import json

from openfisca_core import periods, reforms, simulations


class MaReform(reforms.Reform):

    def __init__(self, tax_benefit_system, ppa_pente=0.5):
        self.ppa_pente = ppa_pente
        super(MaReform, self).__init__(tax_benefit_system)

    def apply(self):
        self.modify_parameters(modifier_function=self.modifier_un_parametre)

    def modifier_un_parametre(self, parameters):
        print("modifier_un_parametre: {}".format(self.ppa_pente))

        # Ceci décrit la periode sur laquelle va s'appliquer ce changement
        reform_year = 2018
        reform_period = periods.period(reform_year)

        # Cette partie propose un changement de taux pour le barème 1 (le second) de l'impôt sur le revenu à partir du début 2017
        parameters.prestations.minima_sociaux.ppa.pente.update(reform_period, value=self.ppa_pente)
        return parameters


def build_scenario(tbs, year, scenario_specific_params):
    scenario_generic_params = {
        "period": year,
        "axes": [
            dict(
                count=20,
                name='salaire_net',
                max=24000,
                min=0,
            )
        ],
    }

    scenario_params = {}
    scenario_params.update(scenario_generic_params)
    scenario_params.update(scenario_specific_params)

    scenario = tbs.new_scenario()
    scenario.init_single_entity(**scenario_params)
    return scenario


def iter_months(year, value):
    for index in range(1, 13):
        yield ("{}-{}".format(year, index), value)


def calcul_ppa_et_salaire(tbs):
    year = '2018'
    decembre = '2018-12'

    celibataire_handicap_567 = {
        "parent1": {
            "age": 29,
            "date_arret_de_travail": "2018-01-30",
            "echelon_bourse": dict(iter_months(year, -1)),
            "gir": dict(iter_months(year, "gir_6")),
            "handicap": dict(iter_months(year, True)),
            "salaire_de_base": dict(iter_months(year, 726.923076923077)),
            "statut_marital": "celibataire",
            "taux_incapacite": dict(iter_months(year, 0.7)),
            "tns_auto_entrepreneur_type_activite": dict(iter_months(year, "bic")),
            "tns_autres_revenus_type_activite": dict(iter_months(year, "bic")),
            "tns_micro_entreprise_type_activite": dict(iter_months(year, "bic")),
        },
        "menage": {
            "loyer": 500,
            "statut_occupation_logement": "locataire_vide",
        },
    }

    scenario = build_scenario(tbs, year, celibataire_handicap_567)
    # scenario.suggest()
    simulation = scenario.new_simulation()

    result_by_variable_name = {}
    for variable_name in ['salaire_net', 'ppa']:
        result_by_variable_name[variable_name] = simulation.calculate(variable_name, period=decembre)

    return result_by_variable_name


def precalculate(france_tbs):
    results = {}
    results[("france", None)] = calcul_ppa_et_salaire(france_tbs)
    for ppa_pente_int in range(0, 101, 10):  # 101 because the highest bound is excluded, and we want to include 100
        ppa_pente = ppa_pente_int / 100.
        reform_tbs = MaReform(france_tbs, ppa_pente)
        results[("reform", ppa_pente_int)] = calcul_ppa_et_salaire(reform_tbs)
    return results


def values_for_ppa_pente(results, ppa_pente_int):
    salaire_net = results[("france", None)]["salaire_net"]
    france_ppa = results[("france", None)]["ppa"]
    reform_ppa = results[("reform", ppa_pente_int)]["ppa"]
    return [salaire_net, france_ppa, reform_ppa]
