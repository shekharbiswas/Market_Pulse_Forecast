import requests
import json
import datetime

# API key and base URL
api_key = <api>
base_url = "https://financialmodelingprep.com/api/v3/stock_news"

# Set the tickers
tickers = "MSFT"

# Function to fetch stock news for a given month and year
def fetch_stock_news(year, month):
    # Format the start and end dates for the month
    start_date = f"{year}-{month:02d}-01"
    # Handle the end date for the month (last day of the month)
    if month == 12:
        end_date = f"{year+1}-01-01"
    else:
        end_date = f"{year}-{month+1:02d}-01"
    
    # Prepare the URL with parameters
    url = f"{base_url}?tickers={tickers}&page=1&from={start_date}&to={end_date}&apikey={api_key}"
    
    # Make the GET request to fetch news
    response = requests.get(url)
    
    # If request is successful, return the JSON data
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {year}-{month:02d}: {response.status_code}")
        return None

# Open a file to save all the JSON data
with open("msft_stock_news_2019_to_present.json", "w") as file:
    # Loop through each year from 2019 to the current year
    for year in range(2019, datetime.datetime.now().year + 1):
        # Loop through each month (January to December)
        for month in range(1, 13):
            print(f"Fetching news for {year}-{month:02d}")
            
            # Fetch the news for the current month and year
            news_data = fetch_stock_news(year, month)
            
            if news_data:
                # Write the news data to the file in JSON format
                file.write(f"--- News for {year}-{month:02d} ---\n")
                json.dump(news_data, file, indent=4)
                file.write("\n\n")

print("News collection complete. Data saved to 'msft_stock_news_2019_to_present.json'.")
