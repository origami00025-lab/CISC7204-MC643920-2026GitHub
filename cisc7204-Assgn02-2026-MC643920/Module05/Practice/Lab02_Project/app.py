from pathlib import Path
import os
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
ROOT=Path(__file__).resolve().parent

df=pd.read_csv(ROOT/'data/Historical_Wildfires.csv')
df['Year']=pd.to_datetime(df.Date).dt.year
df['Month']=pd.to_datetime(df.Date).dt.month
def update_graph(region,year):
    d=df[df.Region.eq(region)&df.Year.eq(year)]
    s=d.groupby('Month',as_index=False)[['Estimated_fire_area','Count']].mean()
    pie=px.pie(s,values='Estimated_fire_area',names='Month',title=f'{region} {year}: Monthly Average Estimated Fire Area')
    bar=px.bar(s,x='Month',y='Count',title=f'{region} {year}: Monthly Average Count of Pixels',labels={'Count':'Mean daily detected pixels'})
    return pie,bar
app=Dash(__name__)
app.layout=html.Div([html.H1('Australia Wildfire Dashboard',style={'textAlign':'center','color':'#503D36','fontSize':26}),html.Div([html.Label('Select Region'),dcc.RadioItems(id='region',options=[{'label':r,'value':r} for r in ['NSW','QL','SA','TA','VI','WA','NT']],value='NSW',inline=True),html.Label('Select Year'),dcc.Dropdown(id='year',options=sorted(df.Year.unique()),value=2005,clearable=False)]),html.Div([html.Div(dcc.Graph(id='pie-chart'),style={'width':'50%'}),html.Div(dcc.Graph(id='bar-chart'),style={'width':'50%'})],style={'display':'flex'})],style={'maxWidth':'1400px','margin':'auto'})
app.callback([Output('pie-chart','figure'),Output('bar-chart','figure')],[Input('region','value'),Input('year','value')])(update_graph)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=int(os.environ.get('PORT','8050')), debug=False)
