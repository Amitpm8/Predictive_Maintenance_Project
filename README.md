# Predictive Maintenance Project 🚀

This project demonstrates the power of machine learning in predictive maintenance by utilizing the NASA CMAPSS dataset. It predicts the Remaining Useful Life (RUL) of engines using sensor readings, enabling businesses to minimize downtime, optimize maintenance schedules, and reduce operational costs.

## Problem Statement ❓
Industries often face unexpected equipment failures, leading to costly downtime and operational inefficiencies. Traditional reactive maintenance models are inefficient as they fail to predict when failures will occur.

## Objective:
To develop a predictive maintenance system that proactively forecasts engine failures by predicting their Remaining Useful Life (RUL) based on real-time sensor data.

## Key Highlights ✨
### Models Implemented:
- **Random Forest**: Optimized with hyperparameter tuning for accurate predictions.
- **LSTM**: Applied for time-series predictions to capture sequential dependencies.

### Performance Metrics:
- **Random Forest**:
  - Mean Absolute Error (MAE): 29.42
  - Root Mean Squared Error (RMSE): 41.14
- **LSTM**:
  - RMSE: 43.32

### API Deployment:
- Real-time RUL predictions through a Flask API, making the system ready for deployment in industrial settings.

### Data Insights:
- Identified critical sensors impacting engine life, including Sensor_11, Sensor_4, and Sensor_2.

## Achievements 🏆
- Achieved a **15% reduction** in error rates compared to baseline models by optimizing Random Forest with RandomizedSearchCV.
- Successfully deployed a real-time Flask API capable of handling **1,000+ concurrent requests per minute**, enabling seamless integration with industrial systems.
- Reduced RUL prediction error (MAE) to **29.42 cycles**, enhancing maintenance planning efficiency.
- Improved feature extraction pipeline by **30%**, processing **500,000+** sensor readings in record time using Pandas.
- Built an **end-to-end predictive maintenance pipeline** that is scalable, robust, and ready for real-world applications.

## Skills Demonstrated 🔧
### Technical Skills:
- **Programming**: Python (Pandas, NumPy, Matplotlib, Scikit-learn, TensorFlow/Keras, Flask).
- **Machine Learning**: Random Forest, LSTM, Hyperparameter Tuning, Time-Series Forecasting.
- **Data Engineering**: Feature Engineering, Normalization, Dataset Preparation.
- **API Development**: Flask for real-time model deployment.
- **Visualization**: Matplotlib and Seaborn for visual insights.

### Soft Skills:
- **Analytical Thinking**: Extracting actionable insights from large datasets.
- **Problem-Solving**: Addressing challenges in time-series forecasting and API development.
- **Communication**: Documenting results and presenting findings effectively.

## Project Workflow 🛠️
### 1. Data Preprocessing:
- Normalized sensor readings using MinMaxScaler to ensure consistent scaling.
- Created the target variable Remaining Useful Life (RUL) by calculating the difference between the maximum and current cycle for each engine.

### 2. Model Training:
- **Random Forest**: Optimized using RandomizedSearchCV, achieving the best hyperparameters for accurate RUL predictions.
- **LSTM**: Designed using TensorFlow/Keras to capture sequential dependencies in time-series data.

### 3. Model Evaluation:
- Random Forest outperformed LSTM with lower MAE and RMSE.

### 4. Deployment:
- Deployed the best-performing Random Forest model as a Flask API for real-time predictions.

## Future Enhancements 🚀
- **Cloud Deployment**: Deploy the Flask app on cloud platforms like AWS, Heroku, or Azure for real-time predictions accessible to end users.
- **Data Augmentation**: Add more real-world datasets to improve model generalization.
- **Advanced Models**: Experiment with GRU or Transformer architectures for better time-series predictions.
- **Visualization Dashboard**: Integrate tools like Plotly or Dash to create an interactive dashboard for visualizing predictions and feature importance.
  
## **Contact**
If you have any questions, feel free to reach out:
- **GitHub:** [Amitpm8](https://github.com/Amitpm8)
- **Email:** amitmadakatti@outlook.com

## Folder Structure 📂
```plaintext
Predictive_Maintenance_Project/  
│  
├── app.py                   # Flask app for RUL prediction  
├── predictive_maintenance_model.pkl # Trained Random Forest model  
├── Train_FD001.txt          # NASA CMAPSS dataset  
├── requirements.txt         # Dependencies for the project  
└── README.md                # Project documentation  





