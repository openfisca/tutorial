# -*- coding: utf-8 -*-

from openfisca_core import periods

import numpy as np

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

# TODO: clean france_ppa
def generate_graph__revenu_disponible(salaire_net, france_ppa, reform_ppa, reform_rsa, reform_revenu_disponible):
    trace1 = go.Scatter(
        name="RSA avec réforme",
        x=salaire_net,
        y=reform_rsa,
        
        mode='lines',
        line=dict(width=0.5,
              color='rgb(184, 247, 212)'),
        fill='tozeroy'
    )

    trace2 = go.Scatter(
        name="Prime d'activité",
        x=salaire_net,
        y=np.array(reform_rsa) + np.array(reform_ppa),

        mode='lines',
        line=dict(width=0.5,
              color='rgb(111, 231, 219)'),
        fill='tozeroy'
    )

    trace3 = go.Scatter(
        name="Revenu disponible",
        x=salaire_net,
        y=reform_revenu_disponible,
        
        mode='lines',
        line=dict(width=0.5,
              color='rgb(127, 166, 238)'),
        # fill='tozeroy'
    )

    data = [trace1, trace2, trace3]

    layout = go.Layout(
        title="Prime d'activité, RSA & Revenu disponible",
        # margin=go.Margin(l=50, r=50, b=50, t=50),
        xaxis={'title': "salaire net (€ par mois)"},
        yaxis={'title': "revenu disponible (€ par mois)"}
    )

    return go.Figure(data=data, layout=layout)
