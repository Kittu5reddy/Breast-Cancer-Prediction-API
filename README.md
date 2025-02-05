# Breast Cancer Prediction Web App

This web application predicts whether a breast cancer tumor is malignant or benign using a machine learning model trained on the Breast Cancer dataset from the `sklearn.datasets` library. It uses Logistic Regression for prediction and is deployed with Flask for a simple web interface.

## Features
- Accepts input of breast cancer features through a web form.
- Provides prediction output: whether the cancer is malignant (cancerous) or benign (non-cancerous).
- Built with Flask, Python, and scikit-learn.

## Installation

### Prerequisites
Ensure that you have Python 3.6 or higher installed.

You also need to install the required libraries, which can be done using `pip`. You can create a virtual environment and install the dependencies.

### Steps to Install:

1. **Clone the repository (or copy the files to your project directory):**

   ```bash
   git clone https://github.com/your-username/breast-cancer-prediction.git
   cd breast-cancer-prediction


   python -m venv venv



   source venv/bin/activate


   pip install -r requirements.txt

   or
pip install flask scikit-learn pandas numpy
   
