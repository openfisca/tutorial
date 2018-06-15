# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import waterfall
from dash.dependencies import Input, Output
from openfisca_core import decompositions, periods
from openfisca_france import FranceTaxBenefitSystem

tbs = FranceTaxBenefitSystem()

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='OpenFisca'),

    html.P(children=[
        "Salaire de base : ",
        html.Span(id="salaire-de-base-value"),
        " € / an",
    ]),
    dcc.Slider(
        id="salaire-de-base",
        min=0,
        max=100000,
        step=300,
        value=20000,
    ),

    html.P(children=[
        "Revenu disponible : ",
        html.Span(id="revenu-disponible", children="loading..."),
        " € / an",
    ]),

    dcc.Graph(
        id='waterfall',
        figure=waterfall.create_figure()
    ),


])


@app.callback(Output('salaire-de-base-value', 'children'), [Input('salaire-de-base', 'value')])
def display_salaire_de_base(salaire_de_base):
    return salaire_de_base


@app.callback(Output('revenu-disponible', 'children'), [Input('salaire-de-base', 'value')])
def calculate_revenu_disponible(salaire_de_base):
    period = 2018

    scenario_params = {
        "period": period,
        "parent1": {
            "age": 30,
            "salaire_de_base": salaire_de_base,
        },
        "enfants": [
            {"age": 6},
            {"age": 8},
            {"age": 10}
        ],
    }

    scenario = tbs.new_scenario().init_single_entity(**scenario_params)
    simulation = scenario.new_simulation()

    revenu_disponible = simulation.calculate("revenu_disponible", period)
    return revenu_disponible


if __name__ == '__main__':
    app.run_server(debug=True, port=7777)
