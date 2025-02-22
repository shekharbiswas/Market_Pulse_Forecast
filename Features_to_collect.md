# Key Features to Collect

## 1. News Features
- **sentiment_score**: Sentiment polarity score of the news article (TextBlob/VADER).  
  Helps assess the emotional tone of news articles (positive, negative, or neutral).
  
- **sentiment_label**: Categorical sentiment (Positive, Neutral, Negative).  
  Converts sentiment score into categorical labels to classify sentiment.

- **news_count_last_24h**: Number of news articles in the last 24 hours for a stock.  
  Provides insight into how much attention the stock is receiving, which may correlate with price movements.

- **average_sentiment_last_24h**: Average sentiment score of news in the last 24 hours.  
  Captures the overall market mood over a short time period.

- **news_volatility_impact**: Sentiment standard deviation (volatility in news).  
  Measures fluctuations in sentiment, which may correlate with stock volatility.


## 2. Stock Price Data
- **open_price**: Opening stock price.  
  Shows the initial price at the beginning of the trading day.

- **close_price**: Closing stock price.  
  Represents the final price at the end of the trading day.

- **high_price**: Highest stock price of the day.  
  Reflects the peak price during the trading day.

- **low_price**: Lowest stock price of the day.  
  Reflects the lowest price during the trading day.

- **volume**: Trading volume (important for liquidity and market movement).  
  Indicates how much of the stock is being traded and helps assess market sentiment.

- **price_change**: Percentage change in stock price ((close - open) / open * 100).  
  Measures the daily price movement, useful for identifying trends.


## 3. Technical Indicators
- **moving_avg_50**: 50-day moving average (trend indicator).  
  A medium-term trend indicator that helps smooth out price data.

- **moving_avg_200**: 200-day moving average (long-term trend).  
  A long-term trend indicator widely used in stock analysis.

- **rsi_14**: Relative Strength Index (momentum indicator).  
  Helps identify overbought or oversold conditions, signaling potential reversals.

- **macd_signal**: MACD signal line (trend strength).  
  Measures the difference between a short-term and long-term moving average, used to identify momentum.

- **bollinger_upper**: Upper Bollinger Band (volatility measure).  
  Helps assess whether a stock is overbought and indicates price volatility.

- **bollinger_lower**: Lower Bollinger Band.  
  Indicates whether a stock is oversold and provides insights into market volatility.

- **atr**: Average True Range (volatility measure).  
  Measures market volatility and potential price movement.

## 4. Additional Features (Not Finalized)

### 4.1. **Lag Features**
- **lagged_features**: Lagged versions of your features, such as `sentiment_score_lag_1`, `price_change_lag_1`, etc.  
  Helps capture temporal dependencies in the data, which is crucial for LSTM models. By including past values, the model can learn sequential patterns over time.

### 4.2. **External Data (Macroeconomic Indicators)**
- **interest_rates**: Central bank interest rate decisions.  
  Changes in interest rates can have a significant impact on stock prices.

- **oil_prices**: Global oil price fluctuations.  
  Can affect market sentiment, especially in energy-related stocks.

### 4.3. **Time-based Features**
- **day_of_week**: Day of the week (Monday, Tuesday, etc.).  
  Stocks often exhibit different behavior on weekdays, with Mondays typically having lower volume.

- **month_of_year**: Month of the year (January, February, etc.).  
  Seasonality can influence stock performance (e.g., end-of-year rallies, tax season effects).

- **holiday_effect**: Indicator for public holidays or major events.  
  Market activity often differs around holidays or important events, affecting stock volatility.


## Conclusion

By combining **sentiment analysis**, **stock price data**, **technical indicators**, and additional features like **lag values** and **macroeconomic data**, we can create a robust model that captures complex relationships and patterns in stock price movements.
