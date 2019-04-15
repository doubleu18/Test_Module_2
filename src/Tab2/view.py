
import dash_core_components as dcc
import dash_html_components as html
from src.master import dfTitanic

def renderTab2():
    return [
            html.Div([
                html.Div([
                    html.P('Jenis : '),
                    dcc.Dropdown(
                        id='jenisplotcategory',
                        options=[{'label' : i, 'value': i} for i in ['Bar','Box','Violin']],
                        value='Bar'
                    )
                ], className='col-3'),
                html.Div([
                    html.P('X : '),
                    dcc.Dropdown(
                        id='xplotcategory',
                        options=[i for i in [{'label' : 'Sex','value' :'sex'},
                                            {'label' : 'Survived','value':'survived'},
                                            {'label' : 'Embark_Town','value':'embark_town'},
                                            {'label' : 'Class','value':'class'},
                                            {'label' : 'Who','value':'who'},
                                            {'label' : 'Alone','value':'alone'},]],
                        value='sex'
                    )
                ], className='col-3'),
                html.Div([
                    html.P('Y : '),
                    dcc.Dropdown(
                        id='yplotcategory',
                        options=[i for i in [{'label' : 'Fare','value' :'fare'},
                                            {'label' : 'Age','value':'age'},]],
                        value='fare'
                    ),
                ], className='col-3'),
                html.Div([
                    html.P('Stats : '),
                    dcc.Dropdown(
                        id='statsplotcategory',
                        options=[i for i in [{'label' : 'Mean','value' :'mean'},
                                            {'label' : 'Standard Deviation','value':'std'},
                                            {'label' : 'Count','value':'count'},
                                            {'label' : 'Max','value':'max'},
                                            {'label' : 'Min','value':'min'},
                                            {'label' : '25th Percentiles','value':'25%'},
                                            {'label' : 'Median','value':'50%'},
                                            {'label' : '75th Percentiles','value':'75%'}]],
                        value='mean',
                        disabled=True
                    ),
                ], className='col-3')
            ], className='row'),
            html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),
            dcc.Graph(
                id='categoryGraph'
            )
        ]