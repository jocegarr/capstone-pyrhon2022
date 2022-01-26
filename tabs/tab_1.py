import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go



x_values = ['2019FY','2020FY','2021FY']
y_values = [30,60,100]
my_data = [go.Bar(
            x=x_values,
            y=y_values,
            marker={'color': ['orange','green','blue']}
            )]
fig_1 = go.Figure(data=my_data)
fig_1



tab_1_layout = html.Div([
    html.H1('Volume'),
    html.H5('Amounts in MM'),
    html.Div([
        dcc.Graph(id='Volume_by_Year', figure=fig_1)])])
