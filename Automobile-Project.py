#!/usr/bin/env python
# coding: utf-8

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# Veriyi yükle
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/d51iMGfp_t0QpO30Lym-dw/automobile-sales.csv')

# Dash uygulamasını başlat
app = dash.Dash(__name__)

# Başlık
app.title = "Automobile Statistics Dashboard"

#---------------------------------------------------------------------------------
# Dropdown seçenekleri
dropdown_options = [
    {'label': 'Yıllık İstatistikler', 'value': 'Yearly Statistics'},
    {'label': 'Resesyon Dönemi İstatistikleri', 'value': 'Recession Period Statistics'}
]
# Yıl listesi
year_list = [i for i in range(1980, 2024, 1)]
#---------------------------------------------------------------------------------------
# Layout (Düzen)
app.layout = html.Div([
    # BAŞLIK
    html.H1("Automobile Sales Statistics Dashboard", 
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 24}),
    
    # DROPDOWN MENÜLER
    html.Div([
        html.Label("Rapor Türünü Seçiniz:"),
        dcc.Dropdown(
            id='dropdown-statistics',
            options=dropdown_options,
            value='Yearly Statistics',
            placeholder='Select Statistics',
            style={'width': '80%', 'padding': '3px', 'font-size': '20px', 'text-align-last': 'center'}
        )
    ]),
    html.Div(dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in year_list],
            value=2005,
            placeholder='Select Year',
            style={'width': '80%', 'padding': '3px', 'font-size': '20px', 'text-align-last': 'center'}
        )),
    
    # ÇIKTI ALANI (GRAFİKLER BURAYA GELECEK)
    html.Div([
        html.Div(id='output-container', className='chart-grid', style={'display': 'flex', 'flex-wrap': 'wrap'}),
    ])
])

# CALLBACK 1: Dropdown etkileşimi (Yıl seçimini aktif/pasif yapma)
@app.callback(
    Output(component_id='select-year', component_property='disabled'),
    Input(component_id='dropdown-statistics', component_property='value'))
def update_input_container(selected_statistics):
    if selected_statistics == 'Yearly Statistics': 
        return False
    else: 
        return True

# CALLBACK 2: Grafikleri oluşturma
@app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='dropdown-statistics', component_property='value'), 
     Input(component_id='select-year', component_property='value')])
def update_output_container(selected_statistics, input_year):
    
    # --- RESESYON DÖNEMİ İSTATİSTİKLERİ ---
    if selected_statistics == 'Recession Period Statistics':
        # Resesyon verisini filtrele
        recession_data = data[data['Recession'] == 1]
        
        # 1. Line Chart: Yıllara göre satış dalgalanması (Fluctuation)
        yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        R_chart1 = dcc.Graph(
            figure=px.line(yearly_rec, 
                x='Year',
                y='Automobile_Sales',
                title="Average Automobile Sales Fluctuation over Recession Period"))

        # 2. Bar Chart: Araç tipine göre satışlar
        average_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()                
        R_chart2 = dcc.Graph(
            figure=px.bar(average_sales,
                x='Vehicle_Type',
                y='Automobile_Sales',
                title="Average Number of Vehicles Sold by Vehicle Type"))
        
        # 3. Pie Chart: Reklam harcamaları dağılımı (Total Advertisement expenditure)
        exp_rec = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        R_chart3 = dcc.Graph(
            figure=px.pie(exp_rec,
                values='Advertising_Expenditure',
                names='Vehicle_Type',
                title="Total Expenditure Share by Vehicle Type during Recessions"
            )
        )

        # 4. Line Plot: İşsizlik oranının satışlara etkisi (Bar yerine Line istendiği için güncellendi)
        # Geri bildirimde "line plot to analyse the effect of the unemployment rate" dendiği için:
        unemp_data = recession_data.groupby(['unemployment_rate', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
        R_chart4 = dcc.Graph(figure=px.line(unemp_data,
            x='unemployment_rate',
            y='Automobile_Sales',
            color='Vehicle_Type',
            title='Effect of Unemployment Rate on Vehicle Type and Sales'))
        
        # 5. EKSTRA: Scatter Plot (Fiyat ve Satış Hacmi İlişkisi) - Geri bildirimde istendi
        R_chart5 = dcc.Graph(
            figure=px.scatter(recession_data,
                x='Price',
                y='Automobile_Sales',
                title='Correlation between Vehicle Price and Sales Volume during Recessions')
        )
        
        # 6. EKSTRA: Bubble Plot (Mevsimsellik Etkisi) - Geri bildirimde istendi
        # Mevsimsellik genellikle ay veya seasonality_weight ile gösterilir.
        R_chart6 = dcc.Graph(
            figure=px.scatter(recession_data,
                x='Month',
                y='Automobile_Sales',
                size='Seasonality_Weight',
                color='Vehicle_Type',
                title='Impact of Seasonality on Automobile Sales (Bubble Plot)')
        )

        return [
            html.Div(className='chart-item', children=[html.Div(children=R_chart1), html.Div(children=R_chart2)], style={'display': 'flex'}),
            html.Div(className='chart-item', children=[html.Div(children=R_chart3), html.Div(children=R_chart4)], style={'display': 'flex'}),
            html.Div(className='chart-item', children=[html.Div(children=R_chart5), html.Div(children=R_chart6)], style={'display': 'flex'})
        ]

    # --- YILLIK İSTATİSTİKLER ---
    elif (input_year and selected_statistics == 'Yearly Statistics'):
        yearly_data = data[data['Year'] == int(input_year)]
                              
        # 1. Yıllık Satış Trendi (Tüm yıllar için)
        yas = data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart1 = dcc.Graph(figure=px.line(yas, 
                                            x='Year', 
                                            y='Automobile_Sales',
                                            title='Yearly Automobile Sales Trend'))
            
        # 2. Aylık Satışlar
        mas = yearly_data.groupby('Month')['Automobile_Sales'].sum().reset_index()
        Y_chart2 = dcc.Graph(figure=px.line(mas,
            x='Month',
            y='Automobile_Sales',
            title='Total Monthly Automobile Sales in {}'.format(input_year)))

        # 3. Araç Tipine Göre Satışlar (Bar)
        avr_vdata = yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        Y_chart3 = dcc.Graph(figure=px.bar(avr_vdata,
                                           x='Vehicle_Type',
                                           y='Automobile_Sales',
                                           title='Average Vehicles Sold by Vehicle Type in {}'.format(input_year)))

        # 4. Reklam Harcamaları (Pie)
        exp_data = yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        Y_chart4 = dcc.Graph(
            figure=px.pie(exp_data, 
            values='Advertising_Expenditure',
            names='Vehicle_Type',
            title='Total Advertisement Expenditure for Each Vehicle in {}'.format(input_year)))
        
        return [
            html.Div(className='chart-item', children=[html.Div(children=Y_chart1), html.Div(children=Y_chart2)], style={'display':'flex'}),
            html.Div(className='chart-item', children=[html.Div(children=Y_chart3), html.Div(children=Y_chart4)], style={'display': 'flex'})
        ]
        
    else:
        return None

# Uygulamayı çalıştır
if __name__ == '__main__':
    # Loading hatası almamak için port ve host belirtildi
    app.run(debug=True, port=8050, host='0.0.0.0')