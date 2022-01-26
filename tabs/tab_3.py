import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

x_values = ['Accepted with Change','Accepted no Change', 'Decline', 'Require Info', 'Lost Deal']
y_values = [1187,562,240,246,73]

data = go.Table(header=dict(values=['Credit Decision', 'Application Count']),
	cells=dict(values=[['Accepted with Change','Accepted no Change', 'Decline', 'Require Info', 'Lost Deal'],
    [1187,562,240,246,73]]
        ))

fig_3 = go.Figure([data])
fig_3



tab_3_layout = html.Div([
    html.H1('Application Activity 2021'),
    html.Div([
        dcc.Graph(id='Application Activity 2021', figure=fig_3)])])
