# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import base64
import datetime
import io

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as pt
import plotly.express as px
import dash_table
from dash.dependencies import Input, Output, State
import os

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {'background': '#111111', 'text': '#7FDBFF'}

app.layout = html.Div(children=[
    html.H1(children='Model Evaluation',
            style={
                'textAlign': 'center',
                'color': colors['text']}),  

    html.Div(children='''
        Model evaluation metircs calculation tool.
    ''', style ={'textAlign': 'center', 'color': colors['text']}),  

    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')]),
        style={
        'width': '100%',
        'height': '60px',
        'lineHeight': '60px',
        'borderWidth': '1px',
        'borderStyle': 'dashed',
        'borderRadius': '5px',
        'textAlign': 'center'
    },
    # Allow multiple files to be upload
    multiple=True
    ),
    dcc.Graph(id='line-plot'),
    html.Div(id='output-data-upload'),
])
    
def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns],
            page_size=10,
            style_table={'height': '300px', 'overflowY': 'auto'}
        ),

        html.Hr()  # horizontal line
    ])

@app.callback(
    Output('line-plot', 'figure'),
    Output('output-data-upload', 'children'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
    State('upload-data', 'last_modified'))
def update_figure(contents, names, dates):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in names:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in names:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])
    df['Date'] = pd.to_datetime(df['Date'])   #Read date
    date = df['Date']
    obs = df['obs']
    sim = df['sim']

    fig = px.line(df, x="Date", y=df.columns,
                hover_data={"Date": "|%B %d, %Y"},
                title='Prediction VS Observation')
    fig.update_xaxes(
        # dtick="M6",
        tickformat="%m\n%Y")
    fig.update_layout(
        xaxis_title = "Date",
        yaxis_title = "",
        legend_title = "")
    return fig
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children

if __name__ == '__main__':
    app.run_server(debug=True)