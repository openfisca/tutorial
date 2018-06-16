# -*- coding: utf-8 -*-

from openfisca_core import periods, reforms


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


def calcul_ppa_et_salaire(tbs):
    year = '2018'
    decembre = '2018-12'

    scenario = tbs.new_scenario().init_single_entity(
        period=year,
        parent1=dict(),
        axes=[
            dict(
                count=20,
                name='salaire_net',
                max=24000,
                min=0,
            )
        ],
    )
    # scenario.suggest()
    simulation = scenario.new_simulation()

    result_by_variable_name = {}
    for variable_name in ['salaire_net', 'ppa', 'rsa']:
        result_by_variable_name[variable_name] = simulation.calculate(variable_name, period=decembre)
    
    for variable_name in ['revenu_disponible']:
        result_by_variable_name[variable_name] = simulation.calculate(variable_name, period=year) / 12
    
    return result_by_variable_name


def precalculate(france_tbs):
    results = {}
    results[("france", None)] = calcul_ppa_et_salaire(france_tbs)
    for ppa_pente_int in range(0, 100, 10):  # 101 because the PPA starts at first 1€ revenue
        ppa_pente = ppa_pente_int / 100.
        reform_tbs = MaReform(france_tbs, ppa_pente)
        results[("reform", ppa_pente_int)] = calcul_ppa_et_salaire(reform_tbs)
    return results


def values_for_ppa_pente(results, ppa_pente_int):
    salaire_net = results[("france", None)]["salaire_net"]
    france_ppa = results[("france", None)]["ppa"]
    
    reform_ppa = results[("reform", ppa_pente_int)]["ppa"]
    reform_rsa = results[("reform", ppa_pente_int)]["rsa"]
    reform_revenu_disponible = results[("reform", ppa_pente_int)]["revenu_disponible"]
    
    return [salaire_net, france_ppa, reform_ppa, reform_rsa, reform_revenu_disponible]
