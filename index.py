import os

import dash
import dash_table as dt
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from sqlalchemy import create_engine
import datetime
from dash.dependencies import Input, Output, State
from plotly import tools
import plotly.graph_objs as go

from src.master import dfTitanic, dfTitanicTable

from src.Tab1.view import renderTab1, generate_table
from src.Tab2.view import renderTab2

from src.Tab1.callbacks import updateCBtable1, updateCBtable2
from src.Tab2.callbacks import updateCBgraph, generateValuePlot



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__)
server=app.server


app.title='Dashboard Titanic'

app.layout = html.Div([
        html.H1('Dashboard Titanic'),
        html.H3('''
                Created By: Brane Warren
                '''),
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Data Titanic', value='tab-1', children = renderTab1()),
        dcc.Tab(label='Categorical Plots', value='tab-2',children = renderTab2()),
    ],style={
        'fontFamily': 'system-ui'
    }, content_style={
        'fontFamily':'Arial',
        'borderBottom' : '1px solid #d6d6d6',
        'borderLeft' : '1px solid #d6d6d6',
        'borderRight' : '1px solid #d6d6d6',
        'padding' : '44px'
    })
], style={
    'maxWidth' : '1200px',
    'margin' : '0 auto'
})

# Tabel
@app.callback(
    Output('table-multicol-sorting', "data"),
    [Input('table-multicol-sorting', "pagination_settings"),
     Input('table-multicol-sorting', "sorting_settings")])
def update_sort_paging_table(pagination_settings, sorting_settings):
    return updateCBtable1(pagination_settings, sorting_settings)

@app.callback(
    Output(component_id='tablediv', component_property='children'),
    [Input('buttonsearch', 'n_clicks'),
    Input('filterrowstable', 'value')],
    [State('filtersurvivedtable', 'value'),
    State('filteragetable', 'value')])
def update_table(n_clicks,maxrows,survived,age):
    return updateCBtable2(n_clicks,maxrows,survived,age)

# Plots
@app.callback(
    Output(component_id='categoryGraph', component_property='figure'),
    [Input(component_id='jenisplotcategory', component_property='value'),
    Input(component_id='xplotcategory', component_property='value'),
    Input(component_id='yplotcategory', component_property='value'),
    Input(component_id='statsplotcategory', component_property='value')])
def update_category_graph(jenisplot, xplot, yplot, statsplot):
    return updateCBgraph(jenisplot, xplot, yplot, statsplot)

# Jenis Plot
@app.callback(
    Output(component_id='statsplotcategory', component_property='disabled'),
    [Input(component_id='jenisplotcategory', component_property='value')])
def update_disabled_stats(jenisplot):
    if jenisplot=='Bar':
        return False
    return True

if __name__ == '__main__':
    app.run_server(debug=True)