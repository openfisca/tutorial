# -*- coding: utf-8 -*-

from openfisca_core import periods
from openfisca_france import FranceTaxBenefitSystem


import plotly.plotly as py
import plotly.graph_objs as go

from ppa_reform import data_frame 

print data_frame

def generate_graph():
    trace1 = go.Scatter(
        x=data_frame['actuel_salaire_net'],
        y=data_frame['actuel_ppa'],
        fill='ppa actuelle'
    )
    trace2 = go.Scatter(
        x=data_frame['actuel_salaire_net'],
        y=data_frame['reforme_ppa'],
        fill='reforme de la ppa'
    )
    data = [trace1, trace2]
    return go.Figure(data=data)
