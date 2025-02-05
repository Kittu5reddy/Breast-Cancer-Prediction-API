# Breast Cancer Classifier

This project is a web application that predicts whether breast cancer is malignant or benign based on user input. It uses a logistic regression model trained on the breast cancer dataset from sklearn.

## Project Structure

- `app.py`: The main Flask application file that handles routing and rendering templates.
- `main.py`: Contains the machine learning model and the prediction logic.
- `static/search.css`: CSS file for styling the web pages.
- `templates/index.html`: (Currently empty) HTML template for the index page.
- `templates/predict.html`: HTML template for displaying the prediction result.
- `templates/search.html`: HTML template for the input form.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```sh
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

3. Enter the required input values in the form and click "Predict" to get the prediction result.

## Input Format

The input should be a comma-separated list of 30 numerical values representing the following features:

## Example Input
[13.54,14.36,87.46,566.3,0.09779,0.08129,0.06664,0.04781,0.1885,0.05766,0.2699,0.7886,2.058,23.56,0.008462,0.0146,0.02387,0.01315,0.0198,0.0023,15.11,19.26,99.7,711.2,0.144,0.1773,0.239,0.1288,0.2977,0.07259]
## License

This project is licensed under the MIT License.