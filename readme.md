# 🐂 Bull's AI: Algorithmic Stock Prediction

## 📊 Empowering Investors with Machine Learning

Bull's AI is an advanced stock price prediction application powered by machine learning. Our platform is designed to help investors make data-driven decisions by leveraging cutting-edge algorithms and real-time market data.

![Bull's AI Logo](https://your-image-url-here.com/bulls-ai-logo.png)

## 🌟 Features

- **Real-time Market Data**: Access the latest stock prices and fundamental metrics
- **Interactive Charts**: Visualize historical data and price predictions with ease
- **ARIMA Forecasting**: Utilize robust statistical models for price predictions
- **Comprehensive Stock Info**: Get detailed information about any listed company
- **User-friendly Interface**: Navigate and analyze stocks with intuitive controls

## 🛠️ Technologies Used

- **[Streamlit](https://streamlit.io/)**: For creating an interactive and user-friendly web interface
- **[YFinance](https://pypi.org/project/yfinance/)**: To fetch real-time and historical financial data from Yahoo Finance
- **[StatsModels](https://www.statsmodels.org/)**: To implement the ARIMA time series forecasting model
- **[Plotly](https://plotly.com/)**: To generate interactive and informative financial charts
- **[Pandas](https://pandas.pydata.org/)**: For data manipulation and analysis

## 🧠 ML Models

Our stock prediction system primarily uses the following models and techniques:

1. **AutoRegressive (AR) Model**: 
   - Part of the ARIMA family of models
   - Implemented using `statsmodels.tsa.ar_model.AutoReg`
   - Uses past stock prices to predict future prices

2. **Time Series Forecasting**:
   - Splits data into training and testing sets
   - Makes predictions on the test set and forecasts 90 days into the future

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/bulls-ai.git
   ```

2. Navigate to the project directory:
   ```
   cd bulls-ai
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```
   streamlit run 🏠Home.py
   ```

5. Open your web browser and go to `http://localhost:8501`

## 📚 How to Use

1. **Stock Info**: Select a stock to view detailed company information and key metrics
2. **Stock Prediction**: Choose a stock, time period, and interval to see price forecasts
3. **Analyze**: Use our interactive charts to spot trends and make informed decisions

## ⚠️ Limitations

- Our AR model assumes that future prices can be predicted based on past prices, which isn't always true in real markets
- The model doesn't account for external factors like company news or economic indicators
- Stock market prediction is inherently challenging and uncertain; use these predictions as one tool among many

## 🔮 Future Improvements

We're constantly working to improve our predictions. Future updates may include:

- Integration of ARIMA or SARIMA models for more complex time series analysis
- Incorporation of machine learning models like Random Forests or Gradient Boosting Machines
- Implementation of deep learning models such as LSTM networks
- Integration of external data sources for more comprehensive analysis

## 👥 Contributing

We welcome contributions to Bull's AI! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) file for details on how to get started.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 👨‍💻 Developers

- [Sahil Bhoite](https://www.linkedin.com/in/sahil-bhoite/): AI & Tech Enthusiast | LLMs | Java Developer | Machine Learning & Data Science Specialist | Python | Pune
- [Maheshwari Jadhav](https://www.linkedin.com/in/maheshwari-jadhav/): Java | Python | AI/ML | Generative AI | Frontend Development | MITAOE'25

