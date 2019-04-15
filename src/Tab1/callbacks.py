import pandas as pd
from sqlalchemy import create_engine
from src.master import dfTitanic, dfTitanicTable, conn, results
from src.Tab1.view import generate_table

def updateCBtable1(pagination_settings, sorting_settings):
    if len(sorting_settings):
        dff = dfTitanicTable.sort_values(
            [col['column_id'] for col in sorting_settings],
            ascending=[
                col['direction'] == 'asc'
                for col in sorting_settings
            ],
            inplace=False
        )
    else:
        # No sort is applied
        dff = dfTitanicTable
    return dff.iloc[
        pagination_settings['current_page']*pagination_settings['page_size']:
        (pagination_settings['current_page'] + 1)*pagination_settings['page_size']
    ].to_dict('rows')    

def updateCBtable2(n_clicks,maxrows,survived,age):
    global dfTitanicTable
    dfTitanicTable = dfTitanic
    if(survived == ''):
         dfTitanicTable = dfTitanicTable[(dfTitanicTable['age']>=age[0]) & (dfTitanicTable['age']<=age[1])]
    elif(survived != ''):
        dfTitanicTable = dfTitanicTable[(dfTitanicTable['survived']==survived) & (dfTitanicTable['age']>=age[0]) & (dfTitanicTable['age']<=age[1])]
    
    return generate_table(dfTitanicTable, pagesize=maxrows)