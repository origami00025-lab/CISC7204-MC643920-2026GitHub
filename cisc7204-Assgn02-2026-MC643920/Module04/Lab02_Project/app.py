from pathlib import Path
import os
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
ROOT=Path(__file__).resolve().parent
airline_data=pd.read_csv(ROOT/'data/airline_data.csv',encoding='ISO-8859-1',low_memory=False)

data=airline_data.sample(n=500,random_state=42)
fig=px.pie(data,values='Flights',names='DistanceGroup',title='Distance group proportion by flights')
app=Dash(__name__)
app.layout=html.Div([html.H1('Airline Dashboard',style={'textAlign':'center','color':'#503D36','fontSize':40}),html.P('Proportion of distance group (250 mile distance interval group) by flights',style={'textAlign':'center','color':'#F57241'}),dcc.Graph(id='distance-pie',figure=fig)],style={'maxWidth':'1200px','margin':'auto'})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=int(os.environ.get('PORT','8050')), debug=False)
