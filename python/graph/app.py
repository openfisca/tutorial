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

import reform_to_graph
import ppa_reform

log = logging.getLogger(__name__)

DEFAULT_TAUX_DEGRESSIVITE_PPA = 0.5

france_tbs = FranceTaxBenefitSystem()

results = ppa_reform.precalculate(france_tbs)
log.debug(results)
import ipdb
ipdb.set_trace()

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
        ),
    ], style={'width': '33%'}),

    html.Div(children=[
        dcc.Graph(
            id='area-chart-ppa',
            figure=reform_to_graph.generate_graph__ppa(data_frame)
        ),

        dcc.Graph(
            id='area-chart-revenu-disponible',
            figure=reform_to_graph.generate_graph__revenu_disponible(data_frame)
        )
    ])

    # un menu permettant de sélectionner la situation et d'afficher le résultat sur la ppa
])


@app.callback(Output('taux-degressivite-ppa-value', 'children'), [Input('taux-degressivite-ppa', 'value')])
def display_taux_degressivite_ppa(taux_degressivite_ppa):
    taux_degressivite_ppa = (taux_degressivite_ppa / 100.)
    return taux_degressivite_ppa


@app.callback(Output('area-chart', 'children'), [Input('taux-degressivite-ppa', 'value')])
def calculate_ppa(taux_degressivite_ppa):
    taux_degressivite_ppa = (taux_degressivite_ppa / 100.)

    print("calculate_ppa > " + str(taux_degressivite_ppa))
    ppa_pente = 1 - taux_degressivite_ppa

    # data_frame = nouvelle_reforme(ppa_pente)
    return reform_to_graph.generate_graph(taux_degressivite_ppa)


if __name__ == '__main__':
    app.run_server(debug=True)
