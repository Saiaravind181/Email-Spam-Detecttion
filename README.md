# Email Spam Detection

This project is a web application built using Streamlit that detects whether an email is spam or not. It uses a pre-trained machine learning model to classify emails based on their content.

## Features

- Allows users to input email text and classifies it as spam or not spam.
- Provides a user-friendly interface with a clean design.
- Utilizes a pre-trained machine learning model for accurate predictions.

## Requirements

- Python 3.x
- Streamlit
- NLTK (Natural Language Toolkit)
- joblib

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Saiaravind181/email-spam-detection.git
    ```

2. Navigate to the project directory:

    ```bash
    cd email-spam-detection
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Download the necessary NLTK data:

    ```python
    import nltk
    nltk.download('stopwords')
    nltk.download('punkt')
    ```

5. Ensure that the pre-trained model files (`vectorizer.pkl` and `model.pkl`) are present in the project directory.

## Usage

1. Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

2. The application will open in your default web browser.

3. Enter the email text in the provided text area.

4. Click the "Classify" button to get the prediction (spam or not spam).

5. The application will display the classification result.

## Dataset

The project uses the `emailspam.csv` dataset, which contains email texts and their corresponding labels (spam or ham).

## Model Training

The model was trained using a Jupyter Notebook (`Email-Spam-Detection.ipynb`). It utilizes TF-IDF vectorization and a machine learning algorithm (e.g., Logistic Regression) to classify emails as spam or not spam.

## Acknowledgments

- The project was inspired by the need for an efficient email spam detection system.
- The dataset used in this project was obtained from a public source.

## License

This project is licensed under the MIT License.
