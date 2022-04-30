from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import requests
import os

BACKEND_URI = os.environ.get("BACKEND_URI", "localhost:8000")


colors = {
    'background': '#7FDBFF',
    'text': '#111111'
}


app = Dash(__name__)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Input(
        id="main-search",
        type="text",
        placeholder="placeholder",
        value="test"
    ),

    html.Div(id="product-name"),

    html.Div(id="product-decision"),

    html.Div(id="product-expiration")
])


@app.callback(
    Output("product-name", "children"),
    Input('main-search', 'value')
)
def get_product_name(product_name: str):
    product_data = requests.get(f"http://{BACKEND_URI}/product/{product_name}").json()
    return f"My product name is {product_data['product_name']}"


@app.callback(
    Output("product-decision", "children"),
    Input('main-search', 'value')
)
def get_product_decision(product_name: str):
    product_data = requests.get(f"http://{BACKEND_URI}/product/{product_name}").json()
    return f"My product decision is {product_data['decision']}"


@app.callback(
    Output("product-expiration", "children"),
    Input('main-search', 'value')
)
def get_product_expiration(product_name: str):
    product_data = requests.get(f"http://{BACKEND_URI}/product/{product_name}").json()
    return f"My product expiration date is {product_data['expiration_date']}"

if __name__ == '__main__':
    app.run_server(debug=True, threaded=True, port=80, host='0.0.0.0')