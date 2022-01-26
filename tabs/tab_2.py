import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go



x_values = ['2019FY','2020FY','2021FY']
y_values = [1623,1954,2308]
my_data = [go.Bar(
        x=x_values,
        y=y_values,
        marker={'color': ['orange','green','blue']}
        )]
fig_2 = go.Figure(data=my_data)
fig_2



tab_2_layout = html.Div([
    html.H1('Application Submissions'),
    html.Div([
        dcc.Graph(id='Applications_by_Year', figure=fig_2)])])
