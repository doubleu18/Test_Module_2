import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt

from src.master import dfTitanicTable, dfTitanicTable

def generate_table(dataframe, pagesize=10):
    return dt.DataTable(
                id='table-multicol-sorting',
                columns=[
                    {"name": i, "id": i} for i in dataframe.columns
                ],
                data=dfTitanicTable.to_dict('rows'),
                style_table={'overflowX': 'scroll'},
                pagination_settings={
                    'current_page': 0,
                    'page_size': pagesize
                },
                pagination_mode='be',
                sorting='be',
                sorting_type='multi',
                sorting_settings=[]
            )      

def renderTab1():
    return [
            html.Div([
                html.Div([
                    html.P('Survived : '),
                    dcc.Dropdown(
                        id='filtersurvivedtable',
                        options=[i for i in [{ 'label': 'All', 'value': '' },
                                            { 'label': 'Survived', 'value': 1 },
                                            { 'label': 'Not-Survived', 'value': 0 }]],
                        value=''
                    )
                ], className='col-4'),
            ], className='row'),
            html.Br(),
            html.Div([
                html.Div([
                    html.P('Age : '),
                    dcc.RangeSlider(
                        marks={i: '{}'.format(i) for i in range(dfTitanicTable['age'].min(), dfTitanicTable['age'].max()+1,5)},
                        min=dfTitanicTable['age'].min(),
                        max=dfTitanicTable['age'].max(),
                        value=[dfTitanicTable['age'].min(),dfTitanicTable['age'].max()],
                        className='rangeslider',
                        id='filteragetable'
                    )
                ], className='col-9'),
                html.Div([
                html.Br(),
                ], className='col-1'),
                html.Div([
                html.Br(),
                    html.Button('Search', id='buttonsearch', style=dict(width='100%'))
                ], className='col-2'),
            ], className='row'),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Div([
                html.Div([
                    html.P('Max Rows : '),
                    dcc.Input(
                        id='filterrowstable',
                        type='number',
                        value=10,
                        style=dict(width='100%')
                    )
                ], className='col-1'),
            ], className='row'),
            html.Center([
                html.H4('Data Titanic', className='title'),
                html.Div(id='tablediv', children=generate_table(dfTitanicTable))
            ])
        ]