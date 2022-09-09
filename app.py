import dash
import dash_bootstrap_components as dbc

from dash import html
from dash import dcc
from dash import Input
from dash import Output

from charts import experience_gantt_chart
from charts import coding_skills_chart
from charts import career_break_chart

#Instantiates the Dash app and identify the server
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

def icon_with_text(icon_name: str = None, text_description: str = None):
    """
    :param icon_name: this is the filename of the icon saved in the directory excluding the .svg extension
    :param text_description: this is the description of the icon relating to a feature I am highlighting
    :return: a dash Container with the text formatted next to the icon
    """

    container = dbc.Container(
        [
            html.Img(src=app.get_asset_url(icon_name + '.svg'), className='feature-icon'),
            html.H2(text_description)
        ], className='icon-with-text'
    )

    return container

def add_tab(tab_name: str = None, tab_id: str = None):
    """

    :param tab_name:
    :param tab_id:
    :return:
    """

    tab = dbc.Tab(label=tab_name,
                  tab_id=tab_id,
                  label_style={"font-family": "GT Haptik", 'font-size' : 18, 'color' : '#19323C', 'border-radius' : '10px 10px 0 0'},
                  active_label_style={"backgroundColor": "#F3F7F0", 'color' : '#19323C'})

    return tab

applayout = [
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Container(
                                [
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    html.Img(src='/assets/headshot.jpg', className='headshot-img')
                                                ], className='headshot-box'
                                            ),
                                            dbc.Col(
                                                [
                                                    html.H1("Hi, I'm Mark!"),
                                                    html.H2("I'm a qualified actuary"),
                                                    html.H2("With a passion for all things data visualisation")
                                                ], className='top-left-box-text'
                                            )
                                        ]
                                    ),
                                ], className='top-left-box'
                            ),
                            dbc.Container(
                                [
                                    dbc.Container(
                                        [
                                            html.H1("Coding Skills:"),
                                            icon_with_text('activity', "18 months applied analytics covering modelling, reporting and visualisation"),
                                            icon_with_text('student', "Always upskilling - recent courses include the basics of data engineering, PySpark, NLP, APIs and HTML / CSS"),
                                            dbc.Button("See my coding skills", className='hero-button')
                                        ], className='bottom-left-box-text'
                                    )
                                ], className='bottom-left-box'
                            ),
                        ], className='left-column'
                    ),
                    dbc.Col(
                        [
                            dbc.Container(
                                [
                                    dbc.Container(
                                        [
                                            html.H1('Experience:'),
                                            icon_with_text('chart-bar', "7 Years across pricing, reserving and capital modelling"),
                                            icon_with_text('presentation-chart', "More recently client a facing technical role at an Insutech"),
                                            icon_with_text('at', "Self taught coding and design work"),
                                            dbc.Button("See my experience", className='hero-button')
                                        ], className='top-right-box-text'
                                    )
                                ], className='top-right-box'
                            ),
                            dbc.Container(
                                [
                                    dbc.Container(
                                        [
                                            html.H1("Career Break:"),
                                            icon_with_text('globe-hemisphere-west', "On qualification I took 10 months out to travel South America."),
                                            html.H2("A few highlights include: spending a month volunteering as an English teacher at a Peruvian school, "
                                                    + "summiting the Cotopaxi volcano (5897m) and completing several multi-day hikes (Machu Picchu – Peru, "
                                                    + "Torres Del Paine – Patagonia, the Ecuadorian Andes and 4 days in the Colombian Jungle)."),
                                            dbc.Button("See my travels", className='hero-button')
                                        ], className='bottom-right-box-text'
                                    )
                                ], className='bottom-right-box'
                            ),
                        ], className='right-column'
                    ),
                ]
            ),
        ], className='features-section'
    ),
    dbc.Container(
        [
            dbc.Card(
                [
                    dbc.CardHeader(
                        dbc.Tabs(
                            [
                                add_tab(tab_name='Experience', tab_id='experience-tab'),
                                add_tab(tab_name='Coding Skills', tab_id='coding-skills-tab'),
                                add_tab(tab_name='Career Break', tab_id='career-break-tab')
                            ], id='card-tabs',
                            active_tab='experience-tab',
                        ), className='card-header'
                    ),
                    dbc.CardBody(
                        [
                            dcc.Graph(id='card-content', className='card-text')
                        ]
                    )
                ], className='charts-card'
            )
        ], className='card-container'
    ),
    dbc.Container(
        [
            dbc.Container(
                [
                    html.H2("Get in touch to request my CV"),
                    html.A(href="mailto: markcooper91@hotmail.co.uk",
                           children=[
                                    html.Img(src=app.get_asset_url('email.png'),
                                            className='contact-img'),
                                    ]
                           ),
                    html.A(href="https://uk.linkedin.com/in/mark-cooper-b8878686",
                           children=[
                                    html.Img(src=app.get_asset_url('linkedin.png'),
                                            className='contact-img')
                                    ]
                           )
                ]
            )
        ], className='contact-container'
    )
]

@app.callback(
    Output("card-content", "figure"),
    Input("card-tabs", "active_tab")
)

def display_chart(active_tab):
    """
    This callback displays the chart data which is dependent on the selected tab
    :param active_tab: the tab which has been selected
    :return: a plotly chart
    """

    if active_tab == 'experience-tab':
        return experience_gantt_chart()
    elif active_tab == 'coding-skills-tab':
        return coding_skills_chart()
    elif active_tab == 'career-break-tab':
        return career_break_chart()
    else:
        return go.Figure()

app.layout = dbc.Container(
    children=applayout,
    fluid=True
)

if __name__ == '__main__':
    app.run_server(debug=True)