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
import plotly.express as px
from dash.dependencies import Input, Output
# import seaborn as sns
import os
# from tkinter import *
# from tkinter import filedialog
# from pandas import ExcelFile
# from pandas import ExcelWriter
# from Basic_cal import BasicStat


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {'background': '#111111', 'text': '#7FDBFF'}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
# fig.update_layout(font_color=colors['text'])


data_path = r"E:\03_Codes\02_codable_2021\backend\Model_eval\streamflow_andong.csv"
data =  pd.read_csv(data_path)
data['Date'] = pd.to_datetime(data['Date'])   #Read date
date = data['Date']
obs = data['obs']
sim = data['sim']

fig = px.line(data, x="Date", y=data.columns,
              hover_data={"Date": "|%B %d, %Y"},
              title='custom tick labels')
fig.update_xaxes(
    dtick="M6",
    tickformat="%m\n%Y")
fig.update_layout(
    xaxis_title = "Date",
    yaxis_title = "",
    legend_title = ""
)


app.layout = html.Div(children=[
    html.H1(children='Model Evaluation',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }),

    html.Div(children='''
        Model evaluation metircs calculation tool.
    ''', style ={'textAlign': 'center', 'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)