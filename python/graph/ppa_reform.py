# -*- coding: utf-8 -*-

from openfisca_core import periods, reforms


class MaReform(reforms.Reform):

    def __init__(self, tax_benefit_system, ppa_pente=0.5):
        self.ppa_pente = ppa_pente
        super(MaReform, self).__init__(tax_benefit_system)

    def apply(self):
        self.modify_parameters(modifier_function=self.modifier_un_parametre)

    def modifier_un_parametre(self, parameters):
        print("modifier_un_parametre > " + str(self.ppa_pente))

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
    for variable_name in ['salaire_net', 'ppa']:
        result_by_variable_name[variable_name] = simulation.calculate(variable_name, period=decembre)

    return result_by_variable_name


def precalculate(france_tbs):
    results = {}
    results[("france", None)] = calcul_ppa_et_salaire(france_tbs)
    for ppa_pente_int in range(0, 100, 10):
        ppa_pente = ppa_pente_int / 100.
        reform_tbs = MaReform(france_tbs, ppa_pente)
        results[("reform", ppa_pente)] = calcul_ppa_et_salaire(reform_tbs)
    return results
