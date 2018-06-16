# -*- coding: utf-8 -*-

from openfisca_core import periods

import plotly.plotly as py
import plotly.graph_objs as go


def generate_graph__ppa(salaire_net, france_ppa, reform_ppa):
    trace1 = go.Scatter(
        name="Législation actuelle",
        x=salaire_net,
        y=france_ppa,
        # fill='tonexty'
    )
    trace2 = go.Scatter(
        name="Réforme",
        x=salaire_net,
        y=reform_ppa,
        # fill='tozeroy'
    )
    data = [trace1, trace2]

    layout = go.Layout(
        title="Prime d'activité par salaire net",
        # margin=go.Margin(l=50, r=50, b=50, t=50),
        xaxis={'title': "salaire net (€ par mois)"},
        yaxis={'title': "prime d'activité (€ par mois)"}
    )

    return go.Figure(data=data, layout=layout)


def generate_graph__revenu_disponible(data_frame):
    trace1 = go.Scatter(
        name="Salaire net",
        x=data_frame['actuel_salaire_net'],
        y=data_frame['actuel_salaire_net'],
        # fill='tonexty'
    )
    trace2 = go.Scatter(
        name="RSA",
        x=data_frame['actuel_salaire_net'],
        y=data_frame['reforme_ppa'],
        # fill='tozeroy'
    )

    trace3 = go.Scatter(
        name="Prime d'activité",
        x=data_frame['actuel_salaire_net'],
        y=data_frame['reforme_ppa'],
        # fill='tozeroy'
    )

    trace4 = go.Scatter(
        name="Revenu disponible",
        x=data_frame['actuel_salaire_net'],
        y=data_frame['reforme_ppa'],
        # fill='tozeroy'
    )

    data = [trace1, trace2, trace3, trace4]

    layout = go.Layout(
        title="Décomposition du revenu disponible",
        # margin=go.Margin(l=50, r=50, b=50, t=50),
        xaxis={'title': "salaire net (€ par mois)"},
        yaxis={'title': "revenu disponible (€ par mois)"}
    )

    return go.Figure(data=data, layout=layout)
