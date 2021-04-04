# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as pt
from dash.dependencies import Input, Output
# import seaborn as sns
import os
# from tkinter import *
# from tkinter import filedialog
# from pandas import ExcelFile
# from pandas import ExcelWriter
# from Basic_cal import BasicStat

df = px.data.iris()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
# data_path = r"E:\03_Codes\02_codable_2021\backend\Model_eval\streamflow_andong.csv"
# data =  pd.read_csv(data_path)
# data['Date'] = pd.to_datetime(data['Date'])   #Read date
# date = data['Date']
# obs = data['obs']
# sim = data['sim']

# pt.figure(figsize= (6,6))
# pt.grid()
# pt.gca().set_aspect("equal")
# # fig = pt.scatter(obs,sim, c=sim, s=5, vmin=min(obs), vmax=max(obs))
# fig = px.scatter(x=date, y=obs)
# pt.colorbar(fig, shrink=0.8)
# pt.plot(obs,obs,label = '1:1')


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Model Performance Assessment Tool',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Assess your model outputs by calculating statistic indice and ploting.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)


