
from dash import Dash, dash_table, dcc, html
import dash
#import plotly.express as px
#import plotly.graph_objects as go
import pandas as pd
import numpy as np
# The data
from app.browserdata import df
#print(df)
df = df.head(101)
#df = pd.read_csv('browserdata.csv')



# Intialise Dash
dapp = Dash(
    __name__,
    # this is essemtial for main app to get page
    requests_pathname_prefix='/dash/',
    # Using prettyer font. Other css is coming straight from assets-folder and thats great.             
    external_stylesheets=["https://fonts.googleapis.com/css2?family=Dosis:wght@200;400;600&display=swap"],
    )

dapp.layout = html.Div([

    html.Div(
        
    ),
    
    html.H2(["Welcome to my Dash page"], className="title"),
    html.Div
    (
        [
            dash_table.DataTable(
            df.to_dict('records'),
            [
                {"name": i, "id": i} for i in df.columns
            ]
            )
        ], className="container"
    )
])

#dapp.run_server(debug=True)
