
## Key Features to Collect

### 1. News Features
- **sentiment_score** – Sentiment polarity score of the news article (TextBlob/VADER).
- **sentiment_label** – Categorical sentiment (Positive, Neutral, Negative).
- **news_count_last_24h** – Number of news articles in the last 24 hours for a stock.
- **average_sentiment_last_24h** – Average sentiment score of news in the last 24 hours.
- **news_volatility_impact** – Sentiment standard deviation (volatility in news).

### 2. Stock Price Data
- **open_price** – Opening stock price.
- **close_price** – Closing stock price.
- **high_price** – Highest stock price of the day.
- **low_price** – Lowest stock price of the day.
- **volume** – Trading volume (important for liquidity and market movement).
- **price_change** – Percentage change in stock price `((close - open) / open * 100)`.

### 3. Technical Indicators
- **moving_avg_50** – 50-day moving average (trend indicator).
- **moving_avg_200** – 200-day moving average (long-term trend).
- **rsi_14** – Relative Strength Index (momentum indicator).
- **macd_signal** – MACD signal line (trend strength).
- **bollinger_upper** – Upper Bollinger Band (volatility measure).
- **bollinger_lower** – Lower Bollinger Band.
- **atr** – Average True Range (volatility measure).

