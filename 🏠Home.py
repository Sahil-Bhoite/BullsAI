import streamlit as st

st.set_page_config(
    page_title="Bull's AI: Algorithmic Stock Prediction",
    page_icon="🐂",
    layout="wide",
)

st.markdown(
    """
    # 🐂 **Bull's AI: Algorithmic Stock Prediction**
    ### **Empowering Investors with Machine Learning**

    **Welcome to Bull's AI, an advanced stock price prediction app powered by machine learning. Our platform is designed to help investors make data-driven decisions by leveraging cutting-edge algorithms and real-time market data.**

    ## 🏗️ **How It's Built**

    Bull's AI is built with these core technologies:

    - **Streamlit** - For creating an interactive and user-friendly web interface
    - **YFinance** - To fetch real-time and historical financial data from Yahoo Finance
    - **StatsModels** - To implement the ARIMA time series forecasting model
    - **Plotly** - To generate interactive and informative financial charts

    ## 🧠 **ML Models and Technical Details**

    Our stock prediction system primarily uses the following models and techniques:

    1. **AutoRegressive (AR) Model**: 
       - Part of the ARIMA family of models
       - Implemented using `statsmodels.tsa.ar_model.AutoReg`
       - Uses past stock prices to predict future prices
       - Configured with a lag order of 250 and heteroskedasticity-robust standard errors

    2. **Time Series Forecasting**:
       - Splits data into training and testing sets
       - Makes predictions on the test set and forecasts 90 days into the future

    3. **Data Processing**:
       - Uses Pandas for data manipulation and analysis
       - Implements data cleaning and preparation techniques

    4. **Visualization**:
       - Utilizes Plotly for creating interactive candlestick charts and line graphs
       - Displays historical data, predictions, and forecast in an easily interpretable format

    ## 🎯 **Key Features**

    - **Real-time Market Data**: Access the latest stock prices and fundamental metrics
    - **Interactive Charts**: Visualize historical data and price predictions with ease
    - **ARIMA Forecasting**: Utilize robust statistical models for price predictions
    - **Comprehensive Stock Info**: Get detailed information about any listed company
    - **User-friendly Interface**: Navigate and analyze stocks with intuitive controls

    ## 📊 **How to Use Bull's AI**

    1. **Stock Info**: Select a stock to view detailed company information and key metrics
    2. **Stock Prediction**: Choose a stock, time period, and interval to see price forecasts
    3. **Analyze**: Use our interactive charts to spot trends and make informed decisions

    ## 🚀 **Get Started**

    Ready to harness the power of AI for your investment decisions? Navigate to the 'Stock Info' or 'Stock Prediction' pages using the sidebar to begin your journey with Bull's AI!

    *Remember: While our AI models are powerful, always combine these insights with your own research and consult with a financial advisor before making investment decisions.*

    ## ⚠️ **Limitations and Considerations**

    - Our AR model assumes that future prices can be predicted based on past prices, which isn't always true in real markets
    - The model doesn't account for external factors like company news or economic indicators
    - Stock market prediction is inherently challenging and uncertain; use these predictions as one tool among many

    ## 🔮 **Future Improvements**

    We're constantly working to improve our predictions. Future updates may include:

    - Integration of ARIMA or SARIMA models for more complex time series analysis
    - Incorporation of machine learning models like Random Forests or Gradient Boosting Machines
    - Implementation of deep learning models such as LSTM networks
    - Integration of external data sources for more comprehensive analysis

    ---
    """
)
