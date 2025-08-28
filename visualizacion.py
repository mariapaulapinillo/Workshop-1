import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go
from kpi import (
    HiresByTechnology,
    HiresByYear,
    HiresBySeniority,
    HiresByCountryOverYears,
    HiresByExperienceRange,
    AverageScores
)

DB_NAME = "Transformation/candidates.db"

df_tech = HiresByTechnology(DB_NAME)
df_year = HiresByYear(DB_NAME)
df_seniority = HiresBySeniority(DB_NAME)
df_country = HiresByCountryOverYears(DB_NAME)
df_experience = HiresByExperienceRange(DB_NAME)
df_avg_scores = AverageScores(DB_NAME)

fig_tech = px.bar(df_tech.sort_values("total_hires", ascending=True),
    x="total_hires", y="technology",
    orientation="h",
    title="Hires by technology")
    
fig_year = px.line(
    df_year, x="year", y="total_hires",
    title="Hires by year"
)
fig_year.update_traces(mode="lines+markers")


fig_seniority = px.pie(
    df_seniority,
    values="total_hires",
    names="seniority",
    title="Distribution of Hires by Seniority"
)

fig_country = px.line(df_country, x="year", y="total_hires",
                      color="country",
                      title="Hires by country (USA, Brazil, Colombia, Ecuador)",
                      markers=True)

fig_experience = px.bar(df_experience, x="experience_range", y="total_hires",
                        title="Hires by experience Range",
                        color="total_hires")

fig_avg_scores = go.Figure()

fig_avg_scores.add_trace(go.Indicator(
    mode="number",
    value=df_avg_scores["avg_code_score"].iloc[0],
    title={"text": "Average Code Challenge"}
))

fig_avg_scores.add_trace(go.Indicator(
    mode="number",
    value=df_avg_scores["avg_interview_score"].iloc[0],
    title={"text": "Average Interview"},
    domain={'row': 1, 'column': 0}
))

fig_avg_scores.update_layout(
    grid={'rows': 2, 'columns': 1, 'pattern': "independent"},
    title="Average scores"
)

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Hiring Dashboard", style={"textAlign": "center"}),

    dcc.Graph(figure=fig_tech),
    dcc.Graph(figure=fig_year),
    dcc.Graph(figure=fig_seniority),
    dcc.Graph(figure=fig_country),
    dcc.Graph(figure=fig_experience),
    dcc.Graph(figure=fig_avg_scores),
])

if __name__ == "__main__":
    app.run(debug=True)

