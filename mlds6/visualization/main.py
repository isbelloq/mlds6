from dash import html, dcc
from dash.dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import plotly.express as px

import json
import os
from mlds6.environment.base import get_data_paths
from mlds6.database.io import load_table
from mlds6.models.model import load_model

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

paths = get_data_paths()
data = {year: load_table(paths.preprocessed_data, f'convocados_{year}', 'parquet')
        for year in range(2016, 2021)}
model = load_model(paths.models, 'DecisionTreeClassifier')
with open(os.path.join(paths.utils_data, 'Colombia2.geo.json')) as f:
    colombia = json.load(f)


app.layout = html.Div(
    [
        html.H1("Secop prediccion sobrecostos"),
        dcc.Slider(id='year-slider',
                   min=2016,
                   max=2020,
                   step=1,
                   marks={year: str(year) for year in range(2016, 2021)},
                   value=2016),
        html.Div(id='chart-results'),
        html.Div(id='table-results')
    ]
)

app.title = 'Secop reporte'


@app.callback(Output('chart-results', 'children'),
              Input('year-slider', 'value')
              )
def set_graph(value):
    if value:
        df = data[value]
        df = df.assign(sobrecosto=lambda df: model.predict(df))

        categories = df.groupby(
            ['sobrecosto']).size().reset_index(name='counts')
        categories['sobrecosto'] = (categories['sobrecosto']
                                    .apply(lambda x: "sobrecosto" if x == 1 else "sin sobrecosto"))

        pie_fig_sobrecosto = px.pie(categories,
                                    names='sobrecosto',
                                    values='counts',
                                    hole=.3)
        graph = dcc.Graph(figure=pie_fig_sobrecosto)

        sobrecosto_por_departamento = (df
                                       .groupby('departamento_entidad')
                                       .agg({'sobrecosto': 'sum'})
                                       .reset_index())

        text = html.P(f'Total datos {value}: {df.shape[0]}', style={
                      'textAlign': 'center', 'fontSize': '35px'})

        colombia_graph = dcc.Graph(figure=px.choropleth(sobrecosto_por_departamento,
                                                        geojson=colombia,
                                                        center={
                                                            'lat': 4, 'lon': -72},
                                                        locations='departamento_entidad',
                                                        fitbounds='geojson',
                                                        color='sobrecosto'))
        title = dbc.Row(
            dbc.Col(text, width=12)
        )
        year_graph = dbc.Row(
            [
                dbc.Col(graph, width=6),
                dbc.Col(colombia_graph, width=6)
            ]
        )
        return [title, year_graph]


@app.callback(Output('table-results', 'children'),
              Input('year-slider', 'value'))
def set_tables(year):
    df = data[year]
    sobrecosto = model.predict(df)
    df = df.assign(sobrecosto=sobrecosto)
    sobrecosto_departamento = (df
                               .groupby('departamento_entidad')
                               .agg({'sobrecosto': 'sum'})
                               .reset_index())
    bar_sobrecostos = dcc.Graph(figure=px.bar(sobrecosto_departamento,
                                              x='departamento_entidad',
                                              y='sobrecosto'))
    total_contratos = "${:,.2f}".format(df['cuantia_contrato'].sum())

    table_header = [
        html.Thead(html.Tr([
            html.Th("Departamento"), html.Th("Sobrecosto")
        ]))
    ]
    departamentos_table = [html.Tbody(
        [
            html.Tr([html.Td(row[1][0]), html.Td(row[1][1])])
            for row in sobrecosto_departamento.iterrows()
        ]
    )]
    info_adiciones_header = [
        html.Thead(html.Tr([
            html.Th("Variable"), html.Th('Total de convocados')
        ]))
    ]

    info_adiciones = [
        html.Tbody(html.Tr([
            html.Td('Cuantía contratos'), html.Td(total_contratos)
        ]))
    ]

    return [dbc.Row(
            [dbc.Col(
                dbc.Table(table_header + departamentos_table, bordered=True),
                width=3
            ), dbc.Col(
                bar_sobrecostos,
                width=6
            ), dbc.Col(
                dbc.Table(info_adiciones_header + info_adiciones, bordered=True),
                width=3
            )
            ])
        ]


if __name__ == '__main__':
    app.run_server(debug=True)
