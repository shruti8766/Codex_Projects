Python Data Science Projects Portfolio
Welcome! This repository contains a collection of three distinct Python projects that demonstrate skills in data analysis, machine learning, and numerical computation using popular libraries such as Pandas, NumPy, Matplotlib, and Scikit-learn.
_______________________________________________________________________________________________
Projects Overview

1. House Price Prediction Using Linear Regression
This project is a complete pipeline to predict house prices based on various features, built using Python and Scikit-learn. The model uses the Kaggle "House Prices - Advanced Regression Techniques" dataset, which consists of 1460 samples and 81 features. The data includes both numerical and categorical attributes.

Dataset: Kaggle "House Prices - Advanced Regression Techniques".

Features: This project includes data preprocessing, such as filling missing values and log-transforming the target variable SalePrice. It also involves feature engineering, creating new features like 

TotalArea. Ordinal categorical variables were encoded into ordered numerical values, and nominal variables were one-hot encoded. A linear regression model was trained and evaluated on the processed data.

Model Performance: The model achieved an RMSE of approximately 0.13 (log scale) and an R2 of 0.86 on the validation set.

Tools: Python, Pandas, NumPy, Matplotlib, and Scikit-learn.

_________________________________________________________________________________________________

2. Data Analysis and Visualization
This project demonstrates core data analysis and visualization skills using Python's data science stack. It involves loading a CSV file, performing basic statistical analysis, and creating various plots to gain insights from the data.

Key Features

Data Analysis: The project uses Pandas to load a CSV file and perform basic tasks like calculating the average of a selected column.

Visualizations: Matplotlib and Seaborn are used to create a variety of plots, including histograms, scatter plots, and correlation heatmaps. A scatter plot, for example, can show the relationship between two variables . The correlation heatmap visualizes the correlation between all numerical features in the dataset .

_______________________________________________________________________________________________

3. Python Matrix Operations Tool Using NumPy
This is an interactive command-line application built with the 

NumPy library that allows users to perform fundamental matrix operations. The application accepts user input for two matrices and provides an interactive menu to select operations.

Key Features

Interactive CLI: The tool provides a command-line interface for users to enter matrix dimensions and elements and choose from a menu of operations.

Matrix Operations: The application supports a range of operations, including addition (A+B), subtraction (A−B), multiplication (A∗B), transpose of a matrix, and determinant calculation.

Error Handling: The tool includes robust validation to ensure matrices have compatible dimensions for each operation (e.g., for addition, matrices must have the same shape) and handles errors gracefully.
___________________________________________________________________________________________

