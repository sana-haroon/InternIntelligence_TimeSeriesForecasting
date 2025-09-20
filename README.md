# InternIntelligence_TimeSeriesForecasting

This repository contains my third internship project for **InternIntelligence** as part of my Data Science remote internship.
## 🚀 Project: Time Series Forecasting
### 📌 Problem Definition
The goal of this project is to build forecasting models that predict future weather trends (temperature, humidity, wind speed, precipitation) using historical data.
### 📊 Dataset
- CSV file containing weather data (Date_Time, Location, Temperature, Humidity, etc.).  
- User uploads their own dataset in the Streamlit app.  
### 🛠️ Steps Followed
1. **Data Preprocessing** – handled missing values, resampled daily averages.  
2. **Model Development** – implemented **ARIMA** and **Prophet** for time series forecasting.  
3. **Model Evaluation** – validated predictions with metrics such as **MAE** and **RMSE**.  
4. **Deployment** – built an interactive **Streamlit application** where users can upload a dataset, choose location/target variable, and generate forecasts.  
### ⚙️ Files in this Repo
- `TimeSeries_Forecasting_Notebook.ipynb` → Jupyter notebook with full analysis  
- `app.py` → Streamlit app for forecasting  
- `requirements.txt` → Dependencies  
### ▶️ How to Run Locally
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/InternIntelligence_TimeSeriesForecasting.git
   cd InternIntelligence_TimeSeriesForecasting
2. Install dependencies:
    ```bash
   pip install -r requirements.txt
3. Run the Streamlit app:
  ```bash
   streamlit run app.py

4.Upload your CSV dataset and view forecasts in the browser.
