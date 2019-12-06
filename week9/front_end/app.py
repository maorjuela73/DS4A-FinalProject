# Import required libraries
import pickle
import copy
import pathlib
import dash
import math
import datetime as dt
import pandas as pd
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html

import flask
import glob
import os

image_directory = '/Users/CamilaMV/Desktop/DS4A-FinalProject/week4-8/front_end/images/'
list_of_images = [os.path.basename(x) for x in glob.glob('{}*.png'.format(image_directory))]
static_image_route = '/static/'


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

######################### Calling Dash ########################

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#app = dash.Dash()
######################### Layout Part ########################

#image_directory = '/Users/chriddyp/Desktop/'
#list_of_images = [os.path.basename(x) for x in glob.glob('{}*.png'.format(image_directory))]
#static_image_route = '/static/'

app.layout = html.Div(
[
    html.Div(
            [
                html.Div(
                    [
                        html.Img(
                            src="/Users/CamilaMV/Desktop/DS4A-FinalProject/week4-8/front_end/img/logotest.png",
                            id="plotly-image",
                            style={
                                "height": "60px",
                                "width": "auto",
                                "margin-bottom": "25px",
                            },
                        )
                    ],
                    className="one-third column",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3(
                                    "AAMovil- Mobile Apps Analysis",
                                    style={"margin-bottom": "0px"},
                                ),
                                html.H5(
                                    "Production Overview", style={"margin-top": "0px"}
                                ),
                            ]
                        )
                    ],
                    className="one-half column",
                    id="title",
                ),
                html.Div(
                    [
                        html.A(
                            html.Button("Learn More", id="learn-more-button"),
                            href="https://github.com/maorjuela73/DS4A-FinalProject",
                        )
                    ],
                    className="one column",
                    id="button",
                ),
            ],
            id="header",
            className="row flex-display",
            style={"margin-bottom": "25px"},
        ),
    html.Div(
        [
            html.Div([
                    html.P(
                        "Search By Name",
                        className="control_label",
                        ),
                    dcc.Input(id='username', value='', type='text'),
                    html.Button(id='submit-button', type='submit', children='Search'),
                    html.Div(id='output_div')

                    ]),
            # TODO: Put space here
            html.Div([
                    html.P(
                        "Choose Stores",
                        className="control_label",
                        ),
                    dcc.Checklist(
                    options=[
                            {'label': 'Google Play Store', 'value': 'Google'},
                            {'label': 'Apple App Store', 'value': 'Apple'}
                            ],
                            value=['Google']
                        )
                    ]),
        ])




])

# app.layout = html.Div(children=[
#     html.Div(
#             children=[
#                 html.H2(children="AAMovil- Mobile Apps Analysis", className='h2-title'),
#             ],
#             className='study-browser-banner row'
#     ),
#         html.Div([
#         dcc.Dropdown(
#             id='image-dropdown',
#             options=[{'label': i, 'value': i} for i in list_of_images],
#             value=list_of_images[0]
#         ),
#         html.Img(id='image')
#         ]
#     )
# ])



######################### Calling back & functions Part ########################
#@app.callback(
#    dash.dependencies.Output('image', 'src'),
#    [dash.dependencies.Input('image-dropdown', 'value')])
#def update_image_src(value):
#    return static_image_route + value

# Add a static image route that serves images from desktop
# Be *very* careful here - you don't want to serve arbitrary files
# from your computer or server
#@app.server.route('{}<image_path>.png'.format(static_image_route))
#def serve_image(image_path):
#    image_name = '{}.png'.format(image_path)
#    if image_name not in list_of_images:
#        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
#    return flask.send_from_directory(image_directory, image_name)



if __name__ == '__main__':
    app.run_server(debug=True)
