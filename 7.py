import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

dados_jogadores = {
    "Jogador": ["Alpha", "Beta", "Gamma", "Delta"],
    "Kills": [120, 95, 135, 110],
    "Dano Causado": [25000, 18500, 30000, 23000],
    "Dano Recebido": [5000, 8000, 4000, 6000],
    "Revives": [3, 5, 1, 2],
    "Precisão (%)": [45.2, 38.4, 50.1, 47.8],
    "Habilidades Usadas": [12, 10, 15, 11],
    "Tempo de Objetivos (min)": [7, 8, 6, 7],
    "Morte por Inimigo Poderoso": [1, 0, 0, 2],  
}

dados_objetivos = {
    "Objetivo": ["Ativar Geradores", "Defender a Base", "Eliminar Terminídios"],
    "Concluído": [True, True, True],
    "Tempo Gasto (min)": [5, 10, 8],
    "Dano Causado": [15000, 18000, 30000],
    "Dano Recebido": [4000, 6000, 12000],
}

df_jogadores = pd.DataFrame(dados_jogadores)
df_objetivos = pd.DataFrame(dados_objetivos)


fig_kda = px.bar(
    df_jogadores,
    x="Jogador",
    y=["Kills", "Dano Causado", "Dano Recebido", "Revives"],
    title="Desempenho Individual (K/D/A/Dano)",
    barmode="group",
    color_discrete_sequence=px.colors.sequential.Viridis,
    text_auto=True,
)
fig_kda.update_layout(paper_bgcolor="#1E1E1E", plot_bgcolor="#1E1E1E", font_color="white")

fig_precisao = px.bar(
    df_jogadores,
    x="Jogador",
    y="Precisão (%)",
    title="Precisão por Jogador",
    text_auto=True,
    color_discrete_sequence=["#00BFFF", "#FF4500", "#32CD32", "#8A2BE2"],
)
fig_precisao.update_layout(paper_bgcolor="#1E1E1E", plot_bgcolor="#1E1E1E", font_color="white")

fig_objetivos = px.bar(
    df_objetivos,
    x="Objetivo",
    y=["Dano Causado", "Dano Recebido"],
    title="Dano Causado e Recebido por Objetivo",
    barmode="group",
    color_discrete_sequence=["#00BFFF", "#FF4500"],
    text_auto=True,
)
fig_objetivos.update_layout(paper_bgcolor="#1E1E1E", plot_bgcolor="#1E1E1E", font_color="white")

app.layout = html.Div(
    style={"backgroundColor": "#1E1E1E", "padding": "20px", "fontFamily": "Arial, sans-serif"},
    children=[
        html.H1(
            "Análise de Partida - Helldivers 2",
            style={"textAlign": "center", "color": "white"},
        ),
        
        html.Div([
            dcc.Graph(figure=fig_kda),
        ], style={"width": "48%", "display": "inline-block"}),

        html.Div([
            dcc.Graph(figure=fig_precisao),
        ], style={"width": "48%", "display": "inline-block"}),

        html.Div([
            dcc.Graph(figure=fig_objetivos),
        ], style={"width": "48%", "display": "inline-block"}),

        html.Footer(
            "Dados fictícios baseados em métricas de partidas de Helldivers 2.",
            style={"textAlign": "center", "color": "white", "marginTop": "20px"},
        ),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
