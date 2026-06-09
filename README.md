# Iris Species Classification Dashboard

A simple and interactive Machine Learning dashboard built with **Streamlit** for predicting Iris flower species based on morphological measurements.

## Overview

This project demonstrates the deployment of a machine learning classification model through a user-friendly web interface.

Users can:

- Input flower measurements manually using sliders
- Upload a CSV file containing flower measurements
- Generate predictions instantly
- Identify the predicted Iris species:
  - Iris Setosa
  - Iris Versicolor
  - Iris Virginica

The application is designed as a portfolio project showcasing the integration of Machine Learning models with interactive dashboards.

---

## Features

### Interactive Prediction Interface
- Manual feature input through sliders
- CSV file upload for batch prediction

### Machine Learning Model Integration
- Pre-trained classification model stored as a Pickle file
- Real-time prediction generation

### User-Friendly Dashboard
- Clean Streamlit interface
- Responsive layout
- Loading indicators during prediction

---

## Input Features

The model uses four botanical measurements:

| Feature | Description |
|----------|-------------|
| Sepal Length (cm) | Length of the sepal |
| Sepal Width (cm) | Width of the sepal |
| Petal Length (cm) | Length of the petal |
| Petal Width (cm) | Width of the petal |

---

## Project Structure

```text
iris_app-main/
│
├── iris_app.py              # Main Streamlit application
├── generate_iris.pkl        # Trained machine learning model
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
