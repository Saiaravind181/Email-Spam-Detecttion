import streamlit as st
from streamlit_lottie import st_lottie
import json
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import joblib
import os

# Ensure the necessary NLTK data packages are downloaded
nltk.download('stopwords')
nltk.download('punkt')

st.set_page_config(
    page_title="Spam Email Detector",
    page_icon="📧",
)

# Custom CSS to style the sidebar
custom_css = """
<style>
    .stButton>button {
        color: white;
        padding: 10px 50px;
        margin: 4px 275px;
        cursor: pointer;
    }
</style>
"""

# Apply the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Load the model and vectorizer using joblib
if os.path.exists('vectorizer.pkl') and os.path.exists('model.pkl'):
    tfidf = joblib.load('vectorizer.pkl')
    model = joblib.load('model.pkl')
else:
    st.error("Model files not found. Ensure 'vectorizer.pkl' and 'model.pkl' are in the directory.")

st.markdown("<h1 style='text-align: center; font-size: 3em;'>📧 Email Spam Detection</h1>", unsafe_allow_html=True)
st.write("")
st.write("")

def load_lottie_file(file_path):
    """
    Load Lottie animation from a local file.
    """
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            lottie_json = json.load(file)
        return lottie_json
    else:
        st.error("Lottie file not found. Ensure the correct path is specified.")
        return None

lottie_file_path = "C:/Users/Aravind/OneDrive/Desktop/mini project/lottie.json"
lottie_json = load_lottie_file(lottie_file_path)

col1, col2 = st.columns([1, 2])

with col1:
    if lottie_json:
        st.lottie(lottie_json, speed=1, width=300, height=300)

with col2:
    # Title and Subtitle
    st.markdown("<h3 style='text-align: center; font-size: 2em;'>Detect whether an email is spam or not.</h3>", unsafe_allow_html=True)

    # Input text area
    input_sms = st.text_area("Enter the message", height=150)

# Predict button
if st.button('Predict'):
    if input_sms:
        # Transform the input message
        transformed_sms = transform_text(input_sms)
        vector_input = tfidf.transform([transformed_sms])
        
        # Check if the model is loaded and then predict
        if 'model' in locals():
            result = model.predict(vector_input)[0]
            st.write("Spam" if result == 1 else "Not Spam")
        else:
            st.error("Prediction model not available. Please check the model file.")
    else:
        st.error("Please enter a message to predict.")
