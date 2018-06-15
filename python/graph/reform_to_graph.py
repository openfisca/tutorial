# -*- coding: utf-8 -*-

from openfisca_core import periods
from openfisca_france import FranceTaxBenefitSystem


import plotly.plotly as py
import plotly.graph_objs as go


tbs = FranceTaxBenefitSystem()


def display_bareme(age, period):
    scenario_params = {
        "period": period,
        "parent1": {
            "age": age,
        },
        "axes": [
            dict(
                count = 10,
                min = 0,
                max = 30000,
                name = 'salaire_de_base',
            ),
        ],
    }
    scenario = tbs.new_scenario().init_single_entity(**scenario_params)
    simulation = scenario.new_simulation()
    ppa = simulation.calculate("ppa", period)

    print(ppa)
    trace1 = go.Scatter(
        x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        y=ppa,
        fill='ppa'
    )
    trace2 = go.Scatter(
        x=[1, 2, 3, 4],
        y=[3, 5, 1, 7],
        fill='tonexty'
    )
    data = [trace1, trace2]
    return go.Figure(data=data)
