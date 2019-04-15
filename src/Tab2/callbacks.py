import plotly.graph_objs as go
from src.master import dfTitanic

listGoFunc = {
    'Bar': go.Bar,
    'Box': go.Box,
    'Violin': go.Violin
}

def generateValuePlot(legendary,xplot,yplot, statsplot = 'mean'):
    return {
        'x': {
            'Bar': dfTitanic[xplot].unique(),
            'Box': dfTitanic[xplot],
            'Violin': dfTitanic[xplot]
        },
        'y': {
            'Bar': dfTitanic.groupby(xplot)[yplot].describe()[statsplot],
            'Box': dfTitanic[yplot],
            'Violin': dfTitanic[yplot]
        }
    }

def updateCBgraph(jenisplot, xplot, yplot, statsplot):
    return dict(
        layout = go.Layout(
                title= '{} Plot Titanic'.format(jenisplot),
                xaxis= {'title': xplot} ,
                yaxis= dict(title=yplot),
                boxmode='group',
                violinmode='group'
            ),
        data=[
            listGoFunc[jenisplot](
                x=generateValuePlot('True',xplot,yplot,)['x'][jenisplot],
                y=generateValuePlot('True',xplot,yplot,statsplot)['y'][jenisplot],
                # name='Mobil Kuno'
            ),
        ]
    )