from pathlib import Path
import os
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
ROOT=Path(__file__).resolve().parent

df=pd.read_csv(ROOT/'data/automobile-sales.csv')
year_list=list(range(1980,2024))
def update_input_container(statistics):
    return statistics != 'Yearly Statistics'
def build_figures(statistics,input_year):
    if statistics=='Recession Period Statistics':
        d=df[df.Recession.eq(1)]
        a=d.groupby('Year',as_index=False).Automobile_Sales.mean()
        b=d.groupby('Vehicle_Type',as_index=False).Automobile_Sales.mean()
        c=d.groupby('Vehicle_Type',as_index=False).Advertising_Expenditure.sum()
        e=d.groupby(['unemployment_rate','Vehicle_Type'],as_index=False).Automobile_Sales.mean()
        return [px.line(a,x='Year',y='Automobile_Sales',title='Average automobile sales during recessions'),px.bar(b,x='Vehicle_Type',y='Automobile_Sales',title='Average sales by vehicle type during recessions'),px.pie(c,names='Vehicle_Type',values='Advertising_Expenditure',title='Advertising expenditure share during recessions'),px.bar(e,x='unemployment_rate',y='Automobile_Sales',color='Vehicle_Type',barmode='group',title='Unemployment rate and sales by vehicle type')]
    if statistics=='Yearly Statistics' and input_year in year_list:
        d=df[df.Year.eq(input_year)]
        a=df.groupby('Year',as_index=False).Automobile_Sales.mean()
        b=d.groupby('Month',as_index=False).Automobile_Sales.sum()
        c=d.groupby('Vehicle_Type',as_index=False).Automobile_Sales.mean()
        e=d.groupby('Vehicle_Type',as_index=False).Advertising_Expenditure.sum()
        return [px.line(a,x='Year',y='Automobile_Sales',title='Yearly average automobile sales — whole period'),px.line(b,x='Month',y='Automobile_Sales',title=f'Total monthly automobile sales in {input_year}'),px.bar(c,x='Vehicle_Type',y='Automobile_Sales',title=f'Average vehicles sold by type in {input_year}'),px.pie(e,names='Vehicle_Type',values='Advertising_Expenditure',title=f'Advertising expenditure by vehicle type in {input_year}')]
    return []
def update_output_container(statistics,input_year):
    figs=build_figures(statistics,input_year)
    return [html.Div(dcc.Graph(figure=f),className='chart-item') for f in figs]
app=Dash(__name__)
app.layout=html.Div([html.H1('Automobile Sales Statistics Dashboard',style={'textAlign':'center','color':'#503D36','fontSize':24}),html.Div([html.Label('Select Report Type'),dcc.Dropdown(id='dropdown-statistics',options=['Yearly Statistics','Recession Period Statistics'],placeholder='Select a report type',value='Select Statistics',clearable=False)]),html.Div([html.Label('Select Year'),dcc.Dropdown(id='select-year',options=year_list,value=2005,placeholder='Select year',clearable=False,disabled=True)]),html.Div(id='output-container',className='chart-grid',style={'display':'grid','gridTemplateColumns':'1fr 1fr'})],style={'maxWidth':'1450px','margin':'auto'})
app.callback(Output('select-year','disabled'),Input('dropdown-statistics','value'))(update_input_container)
app.callback(Output('output-container','children'),[Input('dropdown-statistics','value'),Input('select-year','value')])(update_output_container)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=int(os.environ.get('PORT','8050')), debug=False)
