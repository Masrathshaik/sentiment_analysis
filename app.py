import streamlit as st
import joblib

# Load model & vectorizer
model = joblib.load('models/sentiment_model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

st.title("Sentiment Analysis App")
st.write("Enter customer feedback to predict sentiment (Positive, Negative, Neutral)")

user_input = st.text_area("Feedback here:")

if st.button("Analyze"):
    # Preprocess
    text = user_input.lower()
    text = ''.join([c for c in text if c.isalpha() or c.isspace()])
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    st.success(f"Predicted Sentiment: {prediction}")
