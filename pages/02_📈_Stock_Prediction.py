import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta

# Import helper functions
from helper import *

# Configure the page
st.set_page_config(
    page_title="Stock Price Prediction",
    page_icon="📈",
    layout="wide",
)

# Sidebar
st.sidebar.markdown("## **User Input Features**")

stock_dict = fetch_stocks()
stock = st.sidebar.selectbox("Choose a stock", list(stock_dict.keys()))
stock_exchange = st.sidebar.radio("Choose a stock exchange", ("BSE", "NSE"), index=0)
stock_ticker = f"{stock_dict[stock]}.{'BO' if stock_exchange == 'BSE' else 'NS'}"

st.sidebar.markdown("### **Stock ticker**")
st.sidebar.text_input(label="Stock ticker code", value=stock_ticker, disabled=True)

periods = fetch_periods_intervals()
period = st.sidebar.selectbox("Choose a period", list(periods.keys()))
interval = st.sidebar.selectbox("Choose an interval", periods[period])

# Main content
st.title("📈 Stock Price Prediction")
st.markdown("### Enhance Investment Decisions through Data-Driven Forecasting")

# Fetch stock data
stock_data = fetch_stock_history(stock_ticker, period, interval)

# Historical Data Graph
st.markdown("## Historical Data")

fig_historical = go.Figure(
    data=[
        go.Candlestick(
            x=stock_data.index,
            open=stock_data["Open"],
            high=stock_data["High"],
            low=stock_data["Low"],
            close=stock_data["Close"],
        )
    ]
)
fig_historical.update_layout(
    xaxis_rangeslider_visible=False,
    title=f"{stock} - Historical Price Data",
    yaxis_title="Price (₹)",
)
st.plotly_chart(fig_historical, use_container_width=True)

# Stock Prediction
train_df, test_df, forecast, predictions = generate_stock_prediction(stock_ticker)

if train_df is not None and (forecast >= 0).all() and (predictions >= 0).all():
    st.markdown("## Stock Prediction")

    # Create tabs for different views
    tab1, tab2 = st.tabs(["Prediction Overview", "Detailed Analysis"])

    with tab1:
        # Calculate prediction metrics
        last_price = stock_data["Close"].iloc[-1]
        predicted_price = forecast.iloc[-1]
        price_change = predicted_price - last_price
        price_change_percentage = (price_change / last_price) * 100

        # Display prediction metrics
        col1, col2, col3 = st.columns(3)
        col1.metric("Current Price", f"₹{last_price:.2f}")
        col2.metric("Predicted Price (90 days)", f"₹{predicted_price:.2f}")
        col3.metric("Predicted Change", f"₹{price_change:.2f} ({price_change_percentage:.2f}%)")

        # Simplified prediction graph
        fig_prediction = go.Figure()
        fig_prediction.add_trace(go.Scatter(x=stock_data.index, y=stock_data["Close"], name="Historical", line=dict(color="blue")))
        fig_prediction.add_trace(go.Scatter(x=forecast.index, y=forecast, name="Forecast", line=dict(color="red")))
        fig_prediction.update_layout(
            title=f"{stock} - Price Prediction",
            xaxis_title="Date",
            yaxis_title="Price (₹)",
            legend_title="Data Type",
        )
        st.plotly_chart(fig_prediction, use_container_width=True)

    with tab2:
        # Detailed prediction graph
        fig_detailed = go.Figure()
        fig_detailed.add_trace(go.Scatter(x=train_df.index, y=train_df["Close"], name="Training Data", line=dict(color="blue")))
        fig_detailed.add_trace(go.Scatter(x=test_df.index, y=test_df["Close"], name="Test Data", line=dict(color="green")))
        fig_detailed.add_trace(go.Scatter(x=forecast.index, y=forecast, name="Forecast", line=dict(color="red")))
        fig_detailed.add_trace(go.Scatter(x=test_df.index, y=predictions, name="Test Predictions", line=dict(color="orange")))
        fig_detailed.update_layout(
            title=f"{stock} - Detailed Price Prediction Analysis",
            xaxis_title="Date",
            yaxis_title="Price (₹)",
            legend_title="Data Type",
        )
        st.plotly_chart(fig_detailed, use_container_width=True)

        # Prediction accuracy metrics
        mse = ((test_df["Close"] - predictions) ** 2).mean()
        rmse = mse ** 0.5
        mape = (abs((test_df["Close"] - predictions) / test_df["Close"])).mean() * 100

        st.markdown("### Prediction Accuracy Metrics")
        col1, col2, col3 = st.columns(3)
        col1.metric("Mean Squared Error (MSE)", f"{mse:.2f}")
        col2.metric("Root Mean Squared Error (RMSE)", f"{rmse:.2f}")
        col3.metric("Mean Absolute Percentage Error (MAPE)", f"{mape:.2f}%")

    # Future price table
    st.markdown("### Predicted Future Prices")
    future_dates = pd.date_range(start=forecast.index[-1], periods=5, freq='B')
    future_prices = forecast.reindex(future_dates)
    future_df = pd.DataFrame({
        'Date': future_dates.strftime('%Y-%m-%d'),
        'Predicted Price': future_prices.round(2)
    })
    st.table(future_df)

else:
    st.markdown("## Stock Prediction")
    st.warning("No data available for the selected stock. Please try a different stock or time period.")