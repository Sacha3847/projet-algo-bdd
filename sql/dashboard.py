import pandas as pd
from dash import Dash, dcc, html, Input, Output, dash_table
import plotly.express as px

# =========================
# CHARGEMENT DONNÉES
# =========================

clients = pd.read_csv("data/clients.csv")
produits = pd.read_csv("data/produits.csv")
commandes = pd.read_csv("data/Commandes.csv")
commande_produits = pd.read_csv("data/commande_produits.csv")

# =========================
# FUSION TABLES
# =========================

df = commande_produits.merge(
    produits,
    left_on="produit_id",
    right_on="id"
)

df = df.merge(
    commandes,
    left_on="commande_id",
    right_on="id"
)

# =========================
# CALCULS
# =========================

df["chiffre_affaires"] = df["prix"] * df["quantite"]

df["date_commande"] = pd.to_datetime(df["date_commande"])

# KPI
total_clients = len(clients)
total_commandes = len(commandes)
total_ca = round(df["chiffre_affaires"].sum(), 2)

panier_moyen = round(
    total_ca / total_commandes,
    2
)

quantite_totale = int(df["quantite"].sum())

top_produit = (
    df.groupby("nom")["quantite"]
    .sum()
    .sort_values(ascending=False)
    .idxmax()
)

top_categorie = (
    df.groupby("categorie")["chiffre_affaires"]
    .sum()
    .sort_values(ascending=False)
    .idxmax()
)

# CA PAR JOUR
ca_par_jour = (
    df.groupby("date_commande")["chiffre_affaires"]
    .sum()
    .reset_index()
)

# TABLEAU TOP PRODUITS
top_produits_df = (
    df.groupby("nom")
    .agg({
        "quantite": "sum",
        "chiffre_affaires": "sum"
    })
    .reset_index()
    .sort_values(by="chiffre_affaires", ascending=False)
)

# =========================
# APPLICATION
# =========================

app = Dash(__name__)

# =========================
# STYLE
# =========================

background = "#1e1e2f"
card_color = "#2c2f48"
text_color = "white"

card_style = {
    "backgroundColor": card_color,
    "padding": "20px",
    "borderRadius": "15px",
    "width": "30%",
    "display": "inline-block",
    "margin": "10px",
    "textAlign": "center",
    "color": text_color,
    "boxShadow": "0px 4px 10px rgba(0,0,0,0.3)"
}

# =========================
# LAYOUT
# =========================

app.layout = html.Div([

    html.H1(
        "📊 Dashboard Business Intelligence",
        style={
            "textAlign": "center",
            "color": "white",
            "marginBottom": "30px"
        }
    ),

    # KPI
    html.Div([

        html.Div([
            html.H2(total_clients),
            html.P("Clients")
        ], style=card_style),

        html.Div([
            html.H2(total_commandes),
            html.P("Commandes")
        ], style=card_style),

        html.Div([
            html.H2(f"{total_ca} €"),
            html.P("CA Total")
        ], style=card_style),

        html.Div([
            html.H2(f"{panier_moyen} €"),
            html.P("Panier Moyen")
        ], style=card_style),

        html.Div([
            html.H2(quantite_totale),
            html.P("Produits vendus")
        ], style=card_style),

        html.Div([
            html.H2(top_produit),
            html.P("Top Produit")
        ], style=card_style)

    ], style={
        "display": "flex",
        "flexWrap": "wrap",
        "justifyContent": "center"
    }),

    html.Br(),

    # INFOS BUSINESS
    html.Div([

        html.H3(
            f"🏆 Catégorie la plus rentable : {top_categorie}",
            style={"color": "white"}
        )

    ], style={
        "textAlign": "center"
    }),

    html.Br(),

    # FILTRE
    dcc.Dropdown(
        options=[
            {"label": cat, "value": cat}
            for cat in produits["categorie"].unique()
        ],
        value=produits["categorie"].unique()[0],
        id="filtre-categorie",
        style={
            "width": "50%",
            "margin": "auto"
        }
    ),

    html.Br(),

    # GRAPHIQUE BAR
    dcc.Graph(id="graph-bar"),

    # PIE CHART
    dcc.Graph(id="graph-pie"),

    # COURBE CA
    dcc.Graph(
        figure=px.line(
            ca_par_jour,
            x="date_commande",
            y="chiffre_affaires",
            title="Evolution du chiffre d'affaires",
            markers=True
        ).update_layout(
            paper_bgcolor=background,
            plot_bgcolor=background,
            font_color="white"
        )
    ),

    # TABLEAU
    html.H2(
        "📋 Top Produits",
        style={
            "textAlign": "center",
            "color": "white"
        }
    ),

    dash_table.DataTable(
        data=top_produits_df.to_dict("records"),
        columns=[
            {"name": i, "id": i}
            for i in top_produits_df.columns
        ],
        style_table={"overflowX": "auto"},
        style_cell={
            "textAlign": "center",
            "backgroundColor": "#2c2f48",
            "color": "white"
        },
        style_header={
            "backgroundColor": "#111827",
            "fontWeight": "bold",
            "color": "white"
        }
    )

], style={
    "backgroundColor": background,
    "padding": "20px",
    "fontFamily": "Arial",
    "minHeight": "100vh"
})

# =========================
# CALLBACK
# =========================

@app.callback(
    Output("graph-bar", "figure"),
    Output("graph-pie", "figure"),
    Input("filtre-categorie", "value")
)

def update_graphs(categorie):

    filtre = df[df["categorie"] == categorie]

    graph_bar = px.bar(
        filtre,
        x="nom",
        y="chiffre_affaires",
        color="nom",
        title="Chiffre d'affaires par produit"
    )

    graph_bar.update_layout(
        paper_bgcolor=background,
        plot_bgcolor=background,
        font_color="white"
    )

    graph_pie = px.pie(
        filtre,
        names="nom",
        values="quantite",
        title="Répartition des ventes"
    )

    graph_pie.update_layout(
        paper_bgcolor=background,
        plot_bgcolor=background,
        font_color="white"
    )

    return graph_bar, graph_pie

# =========================
# RUN
# =========================

if __name__ == "__main__":
    app.run(debug=True)

