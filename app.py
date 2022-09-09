import dash
import dash_bootstrap_components as dbc

#Instantiates the Dash app and identify the server
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server