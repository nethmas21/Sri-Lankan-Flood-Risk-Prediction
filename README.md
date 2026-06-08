# Sri-Lankan-Flood-Risk-Prediction Using Machine Learning
Machine Learning and Power BI project for analyzing and predicting flood risk in Sri Lanka using environmental and geographic factors.

## Project Overview

This project aims to analyze flood risk factors in Sri Lanka and develop a machine learning model capable of predicting flood occurrence based on environmental, geographical, and infrastructure-related variables. The project combines Exploratory Data Analysis (EDA), Machine Learning, and Power BI visualization to identify flood-prone regions and understand the key drivers of flooding.

The objective is to support data-driven decision-making by providing insights into flood patterns and demonstrating how predictive analytics can be applied to disaster risk management.

---

## Dataset

The project utilizes a flood risk dataset containing 25,000 records with environmental and geographical information related to flood occurrence.

### Key Features

* Elevation (m)
* Distance to River (m)
* Population Density
* Rainfall (7-Day)
* Monthly Rainfall
* Drainage Index
* Historical Flood Count
* Infrastructure Score
* Flood Risk Score
* Flood Occurrence (Yes/No)

### Dataset Statistics

* Total Records: 25,000
* Flood Events: 2,472
* Non-Flood Events: 22,528
* Flood Percentage: 9.89%

---

## Exploratory Data Analysis (EDA)

Several exploratory analyses were performed to understand flood patterns and relationships between variables.

### Analyses Conducted

* Flood occurrence distribution analysis
* Missing value analysis
* Rainfall pattern analysis
* Top flood-prone district identification
* Correlation analysis
* Feature relationship visualization

### Key Findings

* Flood events represent approximately 9.89% of the dataset.
* Monthly rainfall and 7-day rainfall show strong relationships with flood occurrence.
* Certain districts experience significantly higher flood frequency.
* Environmental factors such as elevation and distance to rivers influence flood risk.

---

## Machine Learning Model

A Random Forest Classification model was developed to predict flood occurrence.

### Model Inputs

* Elevation
* Distance to River
* Population Density
* Rainfall (7-Day)
* Monthly Rainfall
* Drainage Index
* Historical Flood Count
* Infrastructure Score

### Target Variable

* Flood Occurrence (Yes / No)

### Model Evaluation Results

| Metric    | Value  |
| --------- | ------ |
| Accuracy  | 91.16% |
| Precision | 59%    |
| Recall    | 33%    |
| F1 Score  | 43%    |

### Feature Importance Ranking

1. Monthly Rainfall
2. 7-Day Rainfall
3. Elevation
4. Distance to River
5. Drainage Index
6. Infrastructure Score
7. Population Density
8. Historical Flood Count

The model identified rainfall-related variables as the most influential factors affecting flood occurrence.

---

## Power BI Dashboard

An interactive Power BI dashboard was developed to communicate findings effectively.

### Dashboard Pages

### 1. Flood Risk Overview

* Total Records
* Flood Events
* Non-Flood Events
* Flood Percentage
* Flood Occurrence Distribution

### 2. Geographic Risk Analysis

* Top Flood-Prone Districts
* District Filtering
* Flood Risk Score by District
* Geographic Flood Risk Map

### 3. Machine Learning Insights

* Model Accuracy
* Precision
* Recall
* F1 Score
* Feature Importance Visualization
* Key Findings Summary

---

## Results

The project successfully demonstrates the use of machine learning and data visualization techniques for flood risk assessment.

### Major Findings

* Monthly rainfall is the strongest predictor of flooding.
* Short-term rainfall accumulation significantly impacts flood occurrence.
* Areas located closer to rivers are more vulnerable to flooding.
* Lower elevation regions show higher flood susceptibility.
* The Random Forest model achieved 91.16% prediction accuracy.

---

## Technologies Used

### Programming & Analytics

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn

### Data Visualization

* Power BI

### Development Tools

* Visual Studio Code
* Git
* GitHub

---

## Future Improvements

* Integrate real-world meteorological datasets.
* Develop rainfall forecasting models for future flood risk estimation.
* Implement advanced machine learning algorithms such as XGBoost and LightGBM.
* Build a web-based flood risk prediction application using Streamlit.
* Incorporate real-time weather API integration for dynamic flood risk assessment.
* Expand the model to support district-level and province-level forecasting.

---

## Author

Nethma Weerasinghe


