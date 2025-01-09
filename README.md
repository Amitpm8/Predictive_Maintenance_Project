# Predictive Maintenance Project 🚀

This project demonstrates predictive maintenance using machine learning models trained on the **NASA CMAPSS dataset**. The system predicts the **Remaining Useful Life (RUL)** of engines based on sensor readings, enabling proactive maintenance decisions to reduce downtime and costs.

---

## **Key Highlights** ✨
- **Models Used:** Random Forest (optimized via hyperparameter tuning) and LSTM for time-series predictions.
- **API Deployment:** Deployed a Flask API for real-time RUL predictions.
- **Dataset:** NASA CMAPSS data with 21 sensors and operational settings.
- **Performance Metrics:**
  - **Random Forest:**
    - Mean Absolute Error (MAE): **29.42**
    - Root Mean Squared Error (RMSE): **41.14**
  - **LSTM:**
    - RMSE: **43.32**

---

## **Project Workflow** 🛠️
1. **Data Preprocessing:**
   - Normalized sensor readings using MinMaxScaler.
   - Created the target variable **Remaining Useful Life (RUL)**.
2. **Model Training:**
   - Random Forest: Optimized using RandomizedSearchCV.
   - LSTM: Built using TensorFlow/Keras for time-series predictions.
3. **Model Evaluation:**
   - Evaluated models on unseen test data.
4. **Deployment:**
   - Developed a Flask API for real-time RUL predictions.

---

## **How to Use This Project** 🧑‍💻
### **1. Clone the Repository**
```bash
git clone https://github.com/YourUsername/Predictive_Maintenance_Project.git
cd Predictive_Maintenance_Project
