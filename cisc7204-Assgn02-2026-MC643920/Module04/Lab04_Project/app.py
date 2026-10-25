from pathlib import Path
import os
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
ROOT=Path(__file__).resolve().parent
airline_data=pd.read_csv(ROOT/'data/airline_data.csv',encoding='ISO-8859-1',low_memory=False)

DELAY_COLS=['CarrierDelay','WeatherDelay','NASDelay','SecurityDelay','LateAircraftDelay']
IDS=['carrier-plot','weather-plot','nas-plot','security-plot','late-plot']
def compute_info(data,entered_year):
    d=data[data.Year.eq(entered_year)]
    return tuple(d.groupby(['Month','Reporting_Airline'],as_index=False)[col].mean() for col in DELAY_COLS)
def get_graph(entered_year):
    groups=compute_info(airline_data,entered_year)
    return [px.line(d,x='Month',y=c,color='Reporting_Airline',title='Average '+c+' time by airline',labels={c:'Delay (minutes)'}) for d,c in zip(groups,DELAY_COLS)]
app=Dash(__name__)
app.layout=html.Div([html.H1('Flight Delay Time Statistics',style={'textAlign':'center','color':'#503D36','fontSize':30}),html.Div(['Input Year: ',dcc.Input(id='input-year',value=2010,type='number',min=2010,max=2020,step=1,style={'height':'35px','fontSize':30})]),html.Div([dcc.Graph(id=i,style={'width':'50%'}) for i in IDS[:2]],style={'display':'flex'}),html.Div([dcc.Graph(id=i,style={'width':'50%'}) for i in IDS[2:4]],style={'display':'flex'}),dcc.Graph(id=IDS[4])],style={'maxWidth':'1400px','margin':'auto'})
app.callback([Output(i,'figure') for i in IDS],Input('input-year','value'))(get_graph)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=int(os.environ.get('PORT','8050')), debug=False)
