# Project Idea: 
Exploratory Data Analysis on COVID-19 Dataset

## Overview  
This project explores and analyzes the **COVID-19 dataset** using exploratory data analysis (EDA) techniques. The goal is to understand trends, patterns, and insights from the data.  

## Tools and Libraries  
- **Python**  
- **Pandas** for data manipulation  
- **NumPy** for numerical operations  
- **Matplotlib** and **Seaborn** for visualizations  

# The Dataset: 
COVID-19 Pandemic by Our World in Data. 

## **Link**: https://docs.owid.io/projects/etl/api/covid/

## Features(Columns) Description
### **1. country**
The name of the country or region where the data was recorded.

### **2. date**
The specific date when the data was collected or reported.

### **3. total_cases**
The cumulative number of confirmed COVID-19 cases in the country up to the given date.

### **4. new_cases**
The number of newly confirmed COVID-19 cases reported on the given date.

### **5. total_deaths**
The cumulative number of deaths attributed to COVID-19 in the country up to the given date.

### **6. new_deaths**
The number of new deaths attributed to COVID-19 reported on the given date.

### **7. total_cases_per_million**
The cumulative number of COVID-19 cases per one million people in the country. This metric normalizes the data for population size.

### **8. total_deaths_per_million**
The cumulative number of COVID-19 deaths per one million people in the country. This metric allows for fair comparison across countries of different sizes.

### **9. total_vaccinations**
The cumulative number of COVID-19 vaccine doses administered in the country up to the given date.

### **10. people_vaccinated**
The total number of people who have received at least one dose of a COVID-19 vaccine.

### **11. people_fully_vaccinated**
The total number of people who have received all doses required to be fully vaccinated.

### **12. new_vaccinations**
The number of new COVID-19 vaccine doses administered on the given date.

### **13. total_tests**
The cumulative number of COVID-19 tests conducted in the country up to the given date.

### **14. new_tests**
The number of COVID-19 tests conducted on the given date.

### **15. positive_rate**
The percentage of COVID-19 tests that returned positive results on the given date. This helps indicate the spread and testing efficiency.

### **16. population**
The total population of the country, used for normalizing metrics like cases and deaths.

### **17. median_age**
The median age of the population in the country, which may provide insight into demographic factors affecting the impact of COVID-19.

### **18. gdp_per_capita**
The gross domestic product (GDP) per capita of the country, representing the economic output per person, which can help explore correlations between economic factors and COVID-19 outcomes.

# API
I created small api for sharing data between notebooks.

## Endpoints:
- **/raw_data**: to transfer raw data between notebooks.
    - **POST**: to upload the raw data to the api.
    - **GET**: to fetch it from the api.

- **/processed_data**: to transfer processed data between notebooks.
    - **POST**: to upload the processed data to the api.
    - **GET**: to fetch it from the api.
    
# EDA Workflow
## 1. Data Collection

## 2. Data Cleaning & Processing
- 2.1 Handling Missing Values
- 2.2 Handling Duplicates
- 2.3 Date Handling
- 2.4 Feature Engineering

## 3. Data Exploration & Visualization
- 3.1 Univariate Analysis
- 3.2 Bivariate Analysis 
- 3.3 Geospatial Visualization
- 3.4 Time Series Analysis
- 3.5 Multivariate Analysis

## 4. Statistical Analysis
- 4.1 Descriptive Statistics
- 4.2 Trend Analysis
- 4.3 Outlier Detection
- 4.4 Hypothesis Testing

## 5. Insights & Conclusion

# How to Run  

## 1. Clone this repository:  
```
git clone https://github.com/AmeUr56/Covid-19-EDA
```

## 2. Install the required libraries:
```
pip install -r requirements.txt  
```
## 3. Run the API
```
cd API
flask run
```
## 4. Run the Jupyter notebooks or Python scripts to explore the data.

# Contribution
Feel free to contribute by submitting pull requests or reporting issues!

# License
This web app is licensed under the [MIT License](./LICENSE.md).  
Copyright (c) 2024 [Ameur].
