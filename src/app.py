import os

import dash

from data import load_data

from layout import create_layout

from callback import register_callbacks



# Load the combined stock data CSV file

combined_data = load_data(r'C:\Users\Pavithra\OneDrive\Desktop\Projects\stock_market\Input\combined_stock_data.csv')



# Initialize the Dash app

app = dash.Dash(__name__, title="Stock Market Analysis")



# Create a dropdown menu for selecting the ticker

ticker_options = [{'label': ticker, 'value': ticker} for ticker in combined_data['Ticker'].unique()]



# Set the layout of the app

app.layout = create_layout(ticker_options)



# Register callbacks

register_callbacks(app, combined_data)



# Run the Dash app

if __name__ == '__main__':

    port = int(os.environ.get('PORT', 8050))

    app.run(host='0.0.0.0', port=port)