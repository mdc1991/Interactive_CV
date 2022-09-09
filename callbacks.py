from dash.dependencies import Input
from dash.dependencies import Output
from app import app
from charts import experience_gantt_chart
from charts import coding_skills_chart
from charts import career_break_chart
import plotly.graph_objects as go

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

