from pathlib import Path
import os
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
ROOT=Path(__file__).resolve().parent
airline_data=pd.read_csv(ROOT/'data/airline_data.csv',encoding='ISO-8859-1',low_memory=False)

def get_graph(entered_year):
    d=airline_data[airline_data.Year.eq(entered_year)]
    means=d.groupby(['DestState','Reporting_Airline'],as_index=False).Flights.sum()
    return px.bar(means,x='DestState',y='Flights',color='Reporting_Airline',title='Total number of flights to the destination state split by reporting airline')
app=Dash(__name__)
app.layout=html.Div([html.H1('Total number of flights to the destination state split by reporting airline',style={'textAlign':'center','color':'#503D36','fontSize':40}),html.Div(['Input Year: ',dcc.Input(id='input-year',value=2010,type='number',min=2010,max=2020,step=1,style={'height':'50px','fontSize':35})],style={'fontSize':40}),dcc.Graph(id='bar-plot')],style={'maxWidth':'1200px','margin':'auto'})
app.callback(Output('bar-plot','figure'),Input('input-year','value'))(get_graph)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=int(os.environ.get('PORT','8050')), debug=False)
