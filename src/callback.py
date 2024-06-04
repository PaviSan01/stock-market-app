from dash.dependencies import Input, Output
import plotly.express as px

def register_callbacks(app, combined_data):
 @app.callback(
 Output('stock-chart', 'figure'),
 Input('ticker-dropdown', 'value')
 )
 def update_stock_chart(selected_ticker):
    filtered_data = combined_data[combined_data['Ticker'] == selected_ticker]
    fig = px.line(filtered_data, x='Date', y='Close', title=f'{selected_ticker} Stock Price')
    return fig