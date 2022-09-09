import dash_bootstrap_components as dbc
from layouts import applayout
from app import app, server

app.layout = dbc.Container(
    children=applayout,
    fluid=True
)

if __name__ == '__main__':
    app.run_server(debug=True)