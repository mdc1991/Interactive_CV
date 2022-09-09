import pandas as pd
import numpy as np

import plotly.graph_objects as go
import plotly.express as px
import os

colors_hex = {
   'Primary' :  '#19323C',
    'Secondary' : '#F2545B',
    'Tertiary' : '#A93F55'
}

company_font = 'GT Haptik'
title_text_size = 36
regular_text_size = 18


hovertext_template = dict(
                        bgcolor="white",
                        font_size=regular_text_size,
                        font_family=company_font,
                        align='left')

h1 = '<span style="color:' + colors_hex.get(
    'Secondary') + '; font-family: ' + company_font + ';font-weight:bold;font-size: 16;">'
h2 = '<span style="color:' + colors_hex.get(
    'Secondary') + '; font-family: ' + company_font + ';font-style:italic;font-size: 14;">'
h3 = '<span style="color:' + colors_hex.get('Primary') + '; font-family: ' + company_font + ';font-size: 12;">'

def experience_gantt_chart():
    """
    This chart details my experience from 2005-present as a Gantt chart
    :return: a plotly figure
    """

    # Text for Gantt Chart

    school_text = h1 + 'Ilkley Grammar School</span><br>' + \
                  h2 + 'September 2002 - July 2009</span><br>' + \
                  h3 + '<b>GCSEs:</b> <br> - 10 GCSEs A*-B <br><b>A Levels:</b><br> - Mathematics (A) Economics (A) Further Mathematics (B)</span>'

    university_text = h1 + 'Newcastle University</span><br>' + \
                      h2 + 'September 2009 - June 2012</span><br>' + \
                      h3 + 'Degree: Accounting & Mathematics<br>' + 'Grade: 1st Class Hons</span>'

    actuarial_internship_text = h1 + 'Financial Services Authority (FSA) - Actuarial Intern</span><br>' + \
                                h2 + 'September 2012 - January 2013</span><br>' + \
                                h3 + 'I started my actuarial career doing a 4 month internship at the FSA in their<br>' + \
                                'Life & Pensions department. It was a great introduction to what a career in<br>' + \
                                'actuarial may involve. I gained exposure across the actuarial disciplines and<br>' + \
                                ' I decided to apply for jobs in General Insurance.</span>'

    actuarial_analyst_text = h1 + 'Randall & Quilter - Actuarial Analyst</span><br>' + \
                             h2 + 'February 2013 - October 2017</span><br>' + \
                             h3 + 'Specific responsibilities included reserving and pricing analyses for<br>' + \
                             'new and on risk MGAs. Analyses included in depth statistical reviews of<br>' \
                             'their claims history, highlighting key areas of good or poor performance,<br>' \
                             'estimating future performance, sensitivity testing of assumptions and<br>' \
                             'explaining the analyses to senior management.</span>'

    actuarial_exams_text = h1 + 'Actuarial Exams</span><br>' + \
                           h2 + 'February 2013 - June 2017</span><br>' + \
                           h3 + 'It took me 3 1/2 years to pass the 15 exams required to qualify as an actuary. I gained <br>' + \
                           'excellent planning and organisational skills demonstrated by maintaining a solid exam <br>' + \
                           'success rate whilst balancing my work responsibilities. I also learned about motivation<br>' + \
                           'and perseverance through multiple failed exams throughout the road to qualification.<br>' + \
                           'Notable passes include: ST8 (79), SA3 (68), CA3 (67) and ST7 (65).</span>'

    career_break_text = h1 + 'Career Break - South America</span><br>' + \
                        h2 + 'November 2017 - August 2018</span><br>' + \
                        h3 + 'On completion of my Actuarial exams, I took 10 months to travel South America. During<br>' + \
                        'this period, I visited: Argentina, Chile, Bolivia, Peru, Ecuador, Colombia and Brazil. A <br>' + \
                        'few highlights include: spending a month volunteering as an English teacher at a Peruvian <br>' + \
                        'school, summiting the Cotopaxi volcano (5897m), completing several multi-day hikes (Machu <br>' + \
                        'Picchu – Peru, Torres Del Paine – Patagonia, the Ecuadorian Andes and 4 days in the Colombian<br>' + \
                        'Jungle), Carnival in Rio de Janeiro - Brazil, spending time in the Peruvian Amazon, cycling<br>' + \
                        'Death Road and diving with hammerhead sharks in the Galapagos.</span>'

    capital_actuary_text = h1 + 'Coverys - Capital Actuary</span><br>' + \
                           h2 + 'September 2018 - March 2021</span><br>' + \
                           h3 + 'Full range of responsibilities focussed within the Capital Modelling workstream.<br>' + \
                           'These included: being the lead developer on both run-off and live Syndicate capital<br>' + \
                           'models. Analysing, interpreting, questioning, validating and explaining the outputs of<br>' + \
                           'those models to various stakeholders across the business. I began to integreate python<br>' + \
                           'into my day-to-day workflows to improve efficiency across the team. This included an<br>' + \
                           'automated peer review file for model inputs and outputs, quarterly extraction of asset<br>' + \
                           'data in the format required by each capital model which requires the manipulation of<br>' + \
                           'over 300 csv files.</span>'

    technical_consultant_text = h1 + 'Concirrus - Technical Consultant</span><br>' + \
                                h2 + 'April 2021 - Present</span><br>' + \
                                h3 + 'A hands on analytics role supporting the Product, Sales, Customer Success, Data Science<br>' + \
                                'and Marketing teams. My role requires me to be business facing explaining the technicalities<br>' + \
                                'of our product and models to an often non-technical audience. I am heavily involved in Proof<br>' + \
                                'of Concepts (PoCs) aiming to prove value before a feature or model is productionised. I have<br>' + \
                                'helped shape global data strategy by implementing a way of measuring vessel activity at scale<br>' + \
                                'across the globe. I lead the Event Response team creating analyses on hurricanes, oil spills,<br>' + \
                                'the Suez Canal, containership losses and other industry events. I also am the lead visualizer<br>' + \
                                "on a key client's RFPs for new and existing business.</span>"

    df = pd.DataFrame([dict(Task="Ilkley Grammar School (2002-2009)",
                            Start='2008-01-01',
                            Finish='2009-07-31',
                            Resource='Education',
                            Details=school_text),
                       dict(Task="Newcastle University",
                            Start='2009-09-01',
                            Finish='2012-06-30',
                            Resource='Education',
                            Details=university_text),
                       dict(Task="Actuarial Internship",
                            Start='2012-09-01',
                            Finish='2013-01-31',
                            Resource='Employment',
                            Details=actuarial_internship_text),
                       dict(Task="Actuarial Analyst",
                            Start='2013-02-01',
                            Finish='2017-10-13',
                            Resource='Employment',
                            Details=actuarial_analyst_text),
                       dict(Task="Actuarial Qualifications",
                            Start='2013-02-01',
                            Finish='2017-06-30',
                            Resource='Education',
                            Details=actuarial_exams_text),
                       dict(Task="Career Break - South America",
                            Start='2017-11-01',
                            Finish='2018-08-31',
                            Resource='Career Break',
                            Details=career_break_text),
                       dict(Task="Capital Actuary",
                            Start='2018-09-01',
                            Finish='2021-04-02',
                            Resource='Employment',
                            Details=capital_actuary_text),
                       dict(Task="Technical Consultant",
                            Start='2021-04-05',
                            Finish='2022-12-31',
                            Resource='Employment',
                            Details=technical_consultant_text)])
    bar_plot_template = dict(
        layout=go.Layout(paper_bgcolor='#F3F7F0',
                         plot_bgcolor='#F3F7F0',
                         title_font=dict(family=company_font,
                                         size=title_text_size,
                                         color=colors_hex.get('Primary')),
                         font=dict(family=company_font,
                                   size=regular_text_size,
                                   color=colors_hex.get('Primary')),
                         xaxis=dict(gridcolor='white',
                                    showline=True,
                                    linecolor='black'),
                         yaxis=dict(gridcolor='white',
                                    showline=True,
                                    linecolor='black')))

    colors = {'Employment': colors_hex.get('Primary'),
              'Education': colors_hex.get('Secondary'),
              'Career Break': colors_hex.get('Tertiary')}

    fig = px.timeline(df,
                      color='Resource',
                      x_start='Start',
                      x_end='Finish',
                      y='Task',
                      color_discrete_map=colors,
                      custom_data=['Details'])

    fig.update_traces(hovertemplate="%{customdata}")

    fig.update_layout(
        title=dict(text='Experience to Date',
                   font=dict(family=company_font,
                             size=title_text_size),
                   x=0.1,
                   y=0.96
                   ),
        template=bar_plot_template,
        hoverlabel=hovertext_template,
        margin=dict(l=300),
        legend=dict(title=None,
                    yanchor="bottom",
                    y=0.8,
                    xanchor="center",
                    x=0.9,
                    font=dict(size=regular_text_size)
                    )
        )

    fig.update_xaxes(title=None,
                     showspikes=True,
                     spikecolor=colors_hex.get('Primary'),
                     spikethickness=2,
                     range=['2007-12-31', '2022-12-31'])

    fig.update_yaxes(title=None,
                     type='category',
                     categoryorder='array',
                     categoryarray=df['Task'].tolist(),
                     autorange='reversed')

    fig.add_annotation(text="<------ Hover over bars for more details",
                       xref="paper",
                       yref="paper",
                       x=0.12,
                       y=0.97,
                       showarrow=False,
                       align='left',
                       font=dict(family=company_font,
                                 size=regular_text_size,
                                 color=colors_hex.get('Primary')))

    return fig

def coding_skills_chart():
    """
    This function returns the radar chart to display my coding skills
    :return: a plotly figure
    """

    radar_plot_template = dict(
        layout=go.Layout(paper_bgcolor='#F3F7F0',
                         polar=dict(bgcolor='#F3F7F0'),
                         title_font=dict(family=company_font,
                                         size=title_text_size,
                                         color=colors_hex.get('Primary')),
                         font=dict(family=company_font,
                                   size=regular_text_size,
                                   color=colors_hex.get('Primary'))))

    data_viz_text = h1 + 'Data Visualisation</span><br>' + \
                    h3 + 'I started exploring data visualisation techniques in 2017 when I first started learning python. Since<br>' + \
                    'then I have completed kaggle courses on different visualisation methods. When I joined Concirrus I<br>' + \
                    'began to apply what I had learned in my day-to-day workloads. In the last year I have been a member<br>' + \
                    "of the IFoA's Data Visualisation Working Party contributing to an interactive dashboard on French<br>" + \
                    'Third-Party Liability claims. More recently I have been learning how to use Plotly Dash to make<br>' + \
                    'interactive dashboards.</span>'

    dashboards_text = h1 + 'Dashboards</span><br>' + \
                      h3 + 'I have recently been learning how to create interactive dashboards using Plotly Dash. These can be<br>' + \
                      'used in a number of scenarios such as creating low cost proof of concepts for a larger piece of work,<br>' + \
                      'a standardized way of visualising outputs from e.g. a model or to produce automatic reports or<br>' + \
                      'documentation. I am looking to improve my dashboarding capabilities over the coming years.</span>'

    html_text = h1 + 'HTML / CSS</span><br>' + \
                h3 + 'I took a Udemy course on HTML and CSS to better understand how these languages are used when<br>' + \
                'creating dashboards. The course included the fundamentals in both HTML and CSS, Web Design rules,<br>' + \
                'frameworks, components and layout patterns. I have began applying what I have learned when creating<br>' + \
                'dashboards.</span>'

    data_eng_text = h1 + 'Data Engineering</span><br>' + \
                    h3 + 'I am taking a Udemy course on the basics of Data Engineering to better understand how to choose<br>' + \
                    'the right data structures and write more efficient code. Whilst I do not plan to become a data engineer, <br>' + \
                    'this course has given me a useful insight into thinking more about how my code is written and how the<br>' + \
                    'choices I make can impact the scalability of my solutions.</span>'

    nlp_text = h1 + 'Natural Language Processing (NLP)</span><br>' + \
               h3 + 'I took a Udemy course on the basics of NLP and working with textual data. The course covered Python text <br>' + \
               'basics, NLP basics, Part of Speech (POS) Tagging, Named Entity Recognition and Topic Modelling. I have <br>' + \
               'taken the course to improve my ability to process textual data should it become part of my day-to-day workloads.</span>'

    scraping_text = h1 + 'Web Scaping</span><br>' + \
                    h3 + 'I took a tutorial on the basics of webscraping. This course has taught me how to scape data from the internet.<br>' + \
                    'This may open up scenarios in the future where additional data may be available online to use as part of analyses.</span>'

    api_text = h1 + 'APIs</span><br>' + \
               h3 + 'I took a Udemy course on the basics of APIs. This course has taught me how to create a basic Create Read<br>' + \
               'Update Delete (CRUD) API using the Flask API framework. The course included tutorials on creating and hosting<br>' + \
               'SQL databases. I want to understand how APIs work as the efficient flow of data becomes more important.</span>'

    df = pd.DataFrame(dict(
        score=[2, 5, 3, 3, 2, 1, 2],
        discipline=['Data Engineering', 'Data Visualisation', 'Dashboards',
                    'HTML/CSS', 'NLP', 'APIs', 'Web Scraping'],
        text=[data_eng_text, data_viz_text, dashboards_text, html_text, nlp_text, api_text, scraping_text]))

    df = df.sort_values(by='score', ascending=False)

    fig = px.line_polar(df,
                        r='score',
                        theta='discipline',
                        line_close=True,
                        markers=True,
                        line_shape='spline',
                        custom_data=['text'])

    fig.update_traces(hovertemplate="%{customdata}",
                      line=dict(color='#F2545B'))

    fig.layout = dict(title=dict(text='Data Science Skillset',
                                 xanchor='right',
                                 pad=dict(r=200)),
                      template=radar_plot_template,
                      hoverlabel=hovertext_template,
                      margin=dict(r=750))

    #add annotation for hover details
    fig.add_annotation(text="<---------- Hover over markers for more details",
                       xref="paper",
                       yref="paper",
                       x=1.37,
                       y=0.77,
                       showarrow=False,
                       align='left',
                       font=dict(family=company_font,
                                 size=regular_text_size,
                                 color=colors_hex.get('Primary')))

    #add annotation describing the scale
    fig.add_annotation(text="1=Basic, 3=Intermediary, 5=Advanced",
                       xref="paper",
                       yref="paper",
                       x=0.5,
                       y=-0.25,
                       showarrow=False,
                       align='left',
                       font=dict(family=company_font,
                                 size=regular_text_size,
                                 color=colors_hex.get('Primary')))
    return fig

def career_break_chart():
    """
    This function returns a scattermapbox plot of destinations on my career break
    :return: a plotly figure
    """
    scattermap_plot_template = dict(
        layout=go.Layout(paper_bgcolor='#F3F7F0',
                         plot_bgcolor='#F3F7F0',
                         title_font=dict(family=company_font,
                                         size=title_text_size,
                                         color=colors_hex.get('Primary')),
                         font=dict(family=company_font,
                                   size=regular_text_size,
                                   color=colors_hex.get('Primary'))))

    fig = go.Figure(go.Scattermapbox(
        lat=['-51.25', '-0.25', '11.04',
             '-0.68', '-8.10', '-3.75',
             '-22.94', '-16.22', '-13.16'],
        lon=['-72.35', '-90.71', '-73.92',
             '-78.43', '-79.03', '-73.262',
             '-43.21', '-67.78', '-72.54'],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=9,
            color=colors_hex['Secondary']
        ),
        text=["W Trek - Torres Del Paine", "Galapagos Island Tour", "Ciudad Perdida - Lost City Trek",
              "Cotopaxi Volcano Trek", "Volunteering - English Teacher", "Amazon Jungle Expedition - Iquitos",
              "Carnival - Rio de Janeiro", "Death Road - Bolivia", "Machu Picchu - Cusco"],
    ))

    fig.update_layout(
        title=dict(text='Highlights of my South American travels',
                   xanchor='right'
                   ),
        autosize=True,
        template=scattermap_plot_template,
        hovermode='closest',
        hoverlabel=hovertext_template,
        mapbox=dict(
            style='carto-positron',
            center=dict(
                lat=-25,
                lon=-75
            ),
            pitch=0,
            zoom=1.2
        ),
    )

    return fig