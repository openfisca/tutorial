# -*- coding: utf-8 -*-
import dash

# a component for every HTML tag
import dash_html_components as html

# higher-level components that are interactive and are generated 
# with JavaScript, HTML, and CSS through the React.js library
import dash_core_components as dcc


import reform_to_graph


app = dash.Dash()

app.layout = html.Div(children=[
    html.H2(children='#dataFin - Simule ton amendement'),

    html.A(href='https://forum.datafin.fr/t/simule-ton-amendement/214'),

    html.H3("PPA hier et aujourd'hui"),
    dcc.Graph(
        id='example',
        figure=reform_to_graph.generate_graph()
    )

    # slider jouant sur le taux de dégressivité 
    # = 1 - parameters.prestations.minima_sociaux.ppa.pente
    # faire varier le taux de dégressivité entre [0, 1]

    # un menu permettant de sélectionner la situation et d'afficher le résultat sur la ppa
])

if __name__ == '__main__':
    app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
    app.run_server(debug=True)
