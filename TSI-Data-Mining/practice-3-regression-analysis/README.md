This reposity contains homework for the python-based "Data Mining" course, presented for master students of Transport and Telecommunication Institute through collaboration with the University of the West of England (UWE Bristol).

# Computer Practice 3. Regression Analysis Housing Price Prediction Project

## Project Description
This project involves analyzing a housing dataset and building regression models to predict house prices based on various features such as size, number of rooms, condition, view, and more.

## Dataset
- The dataset contains numerical and categorical features describing houses.
- Data cleaning steps include removing outliers based on the 90th percentile.
- Categorical features were converted into dummy variables (one-hot encoding).

## Libraries Used
- pandas
- matplotlib
- seaborn
- scikit-learn
- statsmodels

## Project Workflow
1. Data loading and preprocessing (outlier removal using 90th percentile thresholds)
2. One-hot encoding for categorical variables (`view`, `condition`, `waterfront`)
3. Feature scaling of numerical data using StandardScaler
4. Training and evaluation of a Linear Regression model (metrics: MAE, MSE, RMSE, R²)
5. Training and evaluation of a Random Forest Regressor
6. Visualization of results including scatter plots, residual plots, and error distributions

## Results
- Linear Regression achieved an R² score of approximately 0.54 on the test set.
- Random Forest achieved a training R² score of around 0.94 (test set evaluation pending to check for overfitting).
- Multicollinearity among features was observed during the analysis.
