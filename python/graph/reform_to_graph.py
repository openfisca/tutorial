# -*- coding: utf-8 -*-

from openfisca_core import periods
from openfisca_france import FranceTaxBenefitSystem


import plotly.plotly as py
import plotly.graph_objs as go

from ppa_reform import data_frame 
# print data_frame


def generate_graph():
    trace1 = go.Scatter(
        name="Législation actuelle",
        x=data_frame['actuel_salaire_net'],
        y=data_frame['actuel_ppa'],
        # fill='tonexty'
    )
    trace2 = go.Scatter(
        name="Réforme",
        x=data_frame['actuel_salaire_net'],
        y=data_frame['reforme_ppa'],
        # fill='tozeroy'
    )
    data = [trace1, trace2]
    
    layout = go.Layout(
        title="Prime d'activité par salaire net",
        # margin=go.Margin(l=50, r=50, b=50, t=50),
        xaxis={'title': "salaire net (€)"},
        yaxis={'title': "prime d'activité (€)"}
    )
    
    return go.Figure(data=data, layout=layout)
