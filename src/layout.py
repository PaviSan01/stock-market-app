from dash import dcc, html

def create_layout(ticker_options):
 return html.Div(style={'backgroundColor': 'hashtag#F5F5F5', 'color': 'black'}, children=[
 html.H1("Stock Market Analysis", style={'textAlign': 'center'}),
 html.Div(style={'backgroundColor': 'hashtag#EFEFEF', 'padding': '10px', 'borderRadius': '10px'}, children=[
 dcc.Dropdown(
 id='ticker-dropdown',
 options=ticker_options,
 value=ticker_options[0]['value'],
 style={'width': '100%', 'height': '40px', 'fontSize': '18px', 'color': 'black', 'backgroundColor': 'hashtag#EFEFEF'}
 )
 ]),
 dcc.Graph(id='stock-chart', style={'width': '100%', 'height': '600px'})
 ])