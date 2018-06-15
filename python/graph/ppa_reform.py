# -*- coding: utf-8 -*-

import json
from openfisca_core import periods, reforms
import pandas

from openfisca_france import FranceTaxBenefitSystem


def modifier_un_parametre(parameters):
    # Ceci décrit la periode sur laquelle va s'appliquer ce changement
    reform_year = 2018
    reform_period = periods.period(reform_year)
    # Cette partie propose un changement de taux pour le barème 1 (le second) de l'impôt sur le revenu à partir du début 2017
    parameters.prestations.minima_sociaux.ppa.pente.update(reform_period, value=0.50)
    return parameters

class MaReform(reforms.Reform):

    def apply(self):
        self.modify_parameters(modifier_function = modifier_un_parametre)

reforme_param = MaReform(FranceTaxBenefitSystem())

france = {'systeme':FranceTaxBenefitSystem(), 'calculs':['salaire_net', 'ppa'], 'name': 'actuel'}
ppa_reforme={'systeme':reforme_param, 'calculs':['ppa'], 'name': 'reforme'}
tbs = [france, ppa_reforme]
data_frame = pandas.DataFrame()

def calcul_ppa_et_salaire(calculs_tbs, data_frame_panda):
    calculs = calculs_tbs['calculs']
    tax_benefit_system = calculs_tbs['systeme']
    name = calculs_tbs['name']

    year = 2018
    decembre = '2018-12'

    scenario = tax_benefit_system.new_scenario().init_single_entity(
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
    scenario.suggest()
    json.dumps(scenario.to_json(), ensure_ascii=False, indent=2)
    simulation = scenario.new_simulation()

    for calcul in calculs :
        calcul_name = "{}_{}".format(name,calcul)
        data_frame_panda[calcul_name]=simulation.calculate(calcul, period = decembre)

for system in tbs:
    calcul_ppa_et_salaire(system,data_frame)
print (data_frame)
