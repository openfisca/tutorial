# -*- coding: utf-8 -*-

import logging

import dash
from dash.dependencies import Input, Output

# a component for every HTML tag
import dash_html_components as html

# higher-level components that are interactive and are generated
# with JavaScript, HTML, and CSS through the React.js library
import dash_core_components as dcc

from openfisca_france import FranceTaxBenefitSystem

import ppa_reform
import reform_to_graph

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


france_tbs = FranceTaxBenefitSystem()

results = ppa_reform.precalculate(france_tbs)

DEFAULT_TAUX_DEGRESSIVITE_PPA = 0.5
DEFAULT_PPA_PENTE_INT = 100 - (DEFAULT_TAUX_DEGRESSIVITE_PPA * 100)  # Slider doesn't work with float numbers > moving to integer
DEFAULT_PPA_VALUES = ppa_reform.values_for_ppa_pente(results, ppa_pente_int=DEFAULT_PPA_PENTE_INT)

log.debug(results)

app = dash.Dash()
app.title = '#datFin #214'

# To serve offline, uncomment these lines and check for css dependency:
# app.css.config.serve_locally = True
# app.scripts.config.serve_locally = True
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

# <link rel="stylesheet" type="text/css" href="/css/main.css">
app.layout = html.Div(children=[
    html.H2(children='#dataFin - Simule ton amendement'),

    html.A(href='https://forum.datafin.fr/t/simule-ton-amendement/214'),

    html.Div(children=[
        html.H3("PPA hier et aujourd'hui"),

        # slider jouant sur le taux de dégressivité
        # = 1 - parameters.prestations.minima_sociaux.ppa.pente
        # faire varier le taux de dégressivité entre [0, 1]
        html.P(children=[
            "Taux de dégressivité : ",
            html.Span(id="taux-degressivite-ppa-value")
        ]),
        dcc.Slider(
            id="taux-degressivite-ppa",
            min=0,
            max=100,
            step=10,
            value=DEFAULT_TAUX_DEGRESSIVITE_PPA * 100,
            updatemode='drag',
        ),
    ], style={'width': '33%'}),

    html.Div(children=[
        dcc.Graph(
            id='area-chart-ppa',
            figure=reform_to_graph.generate_graph__ppa(*DEFAULT_PPA_VALUES[:3])
        ),

        dcc.Graph(
            id='area-chart-revenu-disponible',
            figure=reform_to_graph.generate_graph__revenu_disponible(*DEFAULT_PPA_VALUES)
        )
    ])

    # un menu permettant de sélectionner la situation et d'afficher le résultat sur la ppa
])


@app.callback(Output('taux-degressivite-ppa-value', 'children'), [Input('taux-degressivite-ppa', 'value')])
def display_taux_degressivite_ppa(taux_degressivite_ppa_int):
    taux_degressivite_ppa = (taux_degressivite_ppa_int / 100.)
    return taux_degressivite_ppa


@app.callback(Output('area-chart-ppa', 'figure'), [Input('taux-degressivite-ppa', 'value')])
def display_ppa(taux_degressivite_ppa_int):
    ppa_pente_int = 100 - taux_degressivite_ppa_int
    values = ppa_reform.values_for_ppa_pente(results, ppa_pente_int)
    return reform_to_graph.generate_graph__ppa(*values[:3])


@app.callback(Output('area-chart-revenu-disponible', 'figure'), [Input('taux-degressivite-ppa', 'value')])
def display_revenu_disponible(taux_degressivite_ppa_int):
    ppa_pente_int = 100 - taux_degressivite_ppa_int
    values = ppa_reform.values_for_ppa_pente(results, ppa_pente_int)
    return reform_to_graph.generate_graph__revenu_disponible(*values)


if __name__ == '__main__':
    app.run_server(debug=True, port=7777)
