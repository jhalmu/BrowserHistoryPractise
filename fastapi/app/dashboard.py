
from dash import Dash, dash_table, dcc, html
import dash
#import plotly.express as px
#import plotly.graph_objects as go
import pandas as pd
# The data
#from browserdata import df, aika, osoite
#print(df)

df = pd.read_csv('browserdata.csv')


dapp = Dash(
    __name__,
    requests_pathname_prefix='/dash/',             
    external_stylesheets=["https://fonts.googleapis.com/css2?family=Dosis:wght@200;400;600&display=swap"],
    )
#dapp.layout = dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])
dapp.layout = html.Div([
    html.H2(["Welcome to my Dash page"], className="title"),
    html.Div([dash_table.DataTable(df.to_dict('records'),[{"name": i, "id": i} for i in df.columns]
    )], className="container")
])

#dapp.run_server(debug=True)
