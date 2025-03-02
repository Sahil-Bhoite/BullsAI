import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
from datetime import datetime

# Download historical stock data using the yfinance library.
end = datetime.now()
start = datetime(end.year - 20, end.month, end.day)
stock = "GOOG"
google_data = yf.download(stock, start, end)

# Check for and handle missing values in the dataset.
google_data.ffill()  # Forward-fill to handle missing values.

# Plot the adjusted closing price of the stock to visualize its trend.
google_data['Adj Close'].plot(title="Adjusted Closing Price of Google")
plt.xlabel("Years")
plt.ylabel("Adj Close")
plt.show()

# Function to plot columns
def plot_graph(data, column_name):
    data[column_name].plot(figsize=(12, 5), title=f"{column_name} of Google data")
    plt.xlabel("Years")
    plt.ylabel(column_name)
    plt.show()

# Calculated the moving averages to smooth out price data.
google_data['MA_for_100_days'] = google_data['Adj Close'].rolling(100).mean()
google_data['MA_for_250_days'] = google_data['Adj Close'].rolling(250).mean()

# Plot adjusted close price with moving averages
google_data[['Adj Close', 'MA_for_100_days', 'MA_for_250_days']].plot(title="Adjusted Closing Price with Moving Averages")
plt.xlabel("Years")
plt.ylabel("Price")
plt.show()

# To analyze the price change, I calculate the percentage change in the adjusted close price.
google_data['percentage_change_cp'] = google_data['Adj Close'].pct_change()
plot_graph(google_data, 'percentage_change_cp')

# Scale the adjusted close price data to prepare it for the LSTM model.
Adj_close_price = google_data[['Adj Close']].astype(float)
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(Adj_close_price)

# Prepare training data for LSTM
x_data, y_data = [], []
for i in range(100, len(scaled_data)):
    x_data.append(scaled_data[i-100:i])
    y_data.append(scaled_data[i])

# Convert to numpy arrays
x_data, y_data = np.array(x_data), np.array(y_data)

# Split into training and testing sets (70-30 split)
split_len = int(len(x_data) * 0.7)
x_train, x_test = x_data[:split_len], x_data[split_len:]
y_train, y_test = y_data[:split_len], y_data[split_len:]

# Define the LSTM model
model = Sequential([
    LSTM(128, return_sequences=True, input_shape=(x_train.shape[1], 1)),
    Dropout(0.2),  # Add dropout for regularization
    LSTM(64, return_sequences=False),
    Dropout(0.2),
    Dense(25),
    Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(x_train, y_train, batch_size=32, epochs=1)  # Increase batch size, reduce epochs for efficiency

# Summarize the model
model.summary()

# After training, I make predictions and invert the scaling.
predictions = model.predict(x_test)
inv_predictions = scaler.inverse_transform(predictions)
inv_y_test = scaler.inverse_transform(y_test.reshape(-1, 1))

# Calculate the Root Mean Squared Error (RMSE) to assess model performance.
rmse = np.sqrt(np.mean((inv_predictions - inv_y_test) ** 2))
print("RMSE:", rmse)

# Plot actual vs predicted prices
plot_data = pd.DataFrame({
    'Original': inv_y_test.flatten(),
    'Predictions': inv_predictions.flatten()
}, index=google_data.index[split_len + 100:])

plot_data.plot(figsize=(12, 6), title="Actual vs Predicted Prices")
plt.xlabel("Years")
plt.ylabel("Adjusted Close Price")
plt.show()

# Plot the whole data series
combined_data = pd.concat([Adj_close_price[:split_len+100], plot_data], axis=0)
combined_data.plot(figsize=(12, 6), title="Full Data with Predictions")
plt.xlabel("Years")
plt.ylabel("Adjusted Close Price")
plt.show()
