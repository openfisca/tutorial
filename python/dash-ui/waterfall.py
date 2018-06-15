import plotly
import plotly.graph_objs as go

def create_figure():
    x_data = ['Product<br>Revenue', 'Services<br>Revenue',
            'Total<br>Revenue', 'Fixed<br>Costs',
            'Variable<br>Costs', 'Total<br>Costs', 'Total']
    y_data = [400, 660, 660, 590, 400, 400, 340]
    text = ['$430K', '$260K', '$690K', '$-120K', '$-200K', '$-320K', '$370K']

    # Base
    trace0 = go.Bar(
        x=x_data,
        y=[0, 430, 0, 570, 370, 370, 0],
        marker=dict(
            color='rgba(1,1,1, 0.0)',
        )
    )
    # Revenue
    trace1 = go.Bar(
        x=x_data,
        y=[430, 260, 690, 0, 0, 0, 0],
        marker=dict(
            color='rgba(55, 128, 191, 0.7)',
            line=dict(
                color='rgba(55, 128, 191, 1.0)',
                width=2,
            )
        )
    )
    # Costs
    trace2 = go.Bar(
        x=x_data,
        y=[0, 0, 0, 120, 200, 320, 0],
        marker=dict(
            color='rgba(219, 64, 82, 0.7)',
            line=dict(
                color='rgba(219, 64, 82, 1.0)',
                width=2,
            )
        )
    )
    # Profit
    trace3 = go.Bar(
        x=x_data,
        y=[0, 0, 0, 0, 0, 0, 370],
        marker=dict(
            color='rgba(50, 171, 96, 0.7)',
            line=dict(
                color='rgba(50, 171, 96, 1.0)',
                width=2,
            )
        )
    )
    data = [trace0, trace1, trace2, trace3]
    layout = go.Layout(
        title='Annual Profit- 2015',
        barmode='stack',
        paper_bgcolor='rgba(245, 246, 249, 1)',
        plot_bgcolor='rgba(245, 246, 249, 1)',
        showlegend=False
    )

    annotations = []

    for i in range(0, 7):
        annotations.append(dict(x=x_data[i], y=y_data[i], text=text[i],
                                    font=dict(family='Arial', size=14,
                                    color='rgba(245, 246, 249, 1)'),
                                    showarrow=False,))
        layout['annotations'] = annotations

    fig = go.Figure(data=data, layout=layout)
    return fig

# plotly.offline.iplot(fig, filename='waterfall-bar-profit')
