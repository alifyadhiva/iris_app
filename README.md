---
title: Iris Species Classification Demo
emoji: 🌸
colorFrom: pink
colorTo: purple
sdk: streamlit
python_version: "3.10"
app_file: iris_app.py
pinned: false
---

# 🌸 Iris Species Classification Demo

A machine learning-powered Iris flower classification application built with Streamlit.

The application allows users to input flower measurements manually or upload data files and receive instant species predictions based on a trained classification model.

Currently, the model can classify the following three Iris species:

- Iris Setosa
- Iris Versicolor
- Iris Virginica

---

## Overview

This project demonstrates the deployment of a machine learning classification model through an interactive web interface.

The application is designed for educational purposes, machine learning demonstrations, and data science portfolio projects.

---

## Features

- Manual feature input using interactive sliders
- Batch prediction via CSV upload
- Real-time species classification
- Interactive and user-friendly Streamlit dashboard
- Confidence-based prediction output
- Modular project structure for scalability
- Ready for testing and deployment

---

## Supported Classes

| Species |
|----------|
| Iris Setosa |
| Iris Versicolor |
| Iris Virginica |

---

## Input Features

The model uses four flower measurements:

| Feature | Description |
|----------|-------------|
| Sepal Length (cm) | Length of the sepal |
| Sepal Width (cm) | Width of the sepal |
| Petal Length (cm) | Length of the petal |
| Petal Width (cm) | Width of the petal |

---

## Project Structure

```text
.
├── iris_app.py
├── generate_iris.pkl
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

**Linux / macOS**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Model Setup

The trained machine learning model should be stored as:

```text
generate_iris.pkl
```

If you wish to use a different model, update the model path in the application source code.

---

## Running the Application

Start the Streamlit application:

```bash
streamlit run iris_app.py
```

The dashboard will be available locally at:

```text
http://localhost:8501
```

---

## CSV Upload Format

For batch prediction, upload a CSV file with the following columns:

```csv
SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm
5.1,3.5,1.4,0.2
6.2,2.9,4.3,1.3
7.1,3.0,5.9,2.1
```

---

## Technology Stack

- Python 3.10
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Pickle

---

## Use Cases

- Machine Learning deployment demonstrations
- Educational projects and tutorials
- Data Science portfolio showcases
- Classification model demonstrations
- Streamlit application examples

---

## Future Improvements

- Prediction probability visualization
- Model performance metrics dashboard
- Batch prediction export functionality
- Feature importance analysis
- Additional classification models for comparison
- Enhanced user interface and visualizations

---

## Disclaimer

This application is intended for educational, research, and demonstration purposes. Prediction accuracy depends on the quality of the trained model and the validity of the input data.

---

## Author

**Alifya Awalia Dhiva**

Data Analyst | GIS Analyst | Geology & Mining Professional

- LinkedIn: https://www.linkedin.com/in/alifyadhiva/

---

## License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project for educational and research purposes.
