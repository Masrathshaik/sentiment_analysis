📊 Sentiment Analysis using NLP

This project applies Natural Language Processing (NLP) techniques to analyze customer feedback and classify sentiment as Positive, Negative, or Neutral.

It includes:

Data preprocessing (cleaning text, removing stopwords)

Feature extraction with TF-IDF Vectorization

Classification using Naive Bayes

A Streamlit web app for live predictions

🚀 Features

Preprocess raw customer feedback

Train a sentiment classification model

Real-time sentiment prediction via web interface

Easy deployment with Streamlit Cloud

🛠️ Tools & Libraries

Python 3.8+

NLTK

Scikit-learn

Pandas, NumPy

Streamlit

Joblib

📂 Project Structure
sentiment_analysis/
├── data/
│   └── feedback.csv          # Sample dataset
├── models/
│   ├── sentiment_model.pkl   # Trained model
│   └── vectorizer.pkl        # TF-IDF vectorizer
├── sentiment_analysis.ipynb  # Model training notebook
├── app.py                    # Streamlit web app
├── requirements.txt          # Dependencies
└── README.md                 # Project documentation

📊 Dataset

A simple CSV dataset (data/feedback.csv) with customer feedback and sentiment labels:
text,sentiment
"I love this product!",positive
"The service was terrible.",negative
"Average experience.",neutral

🌐 Deployment

This project can be deployed easily using Streamlit Cloud:

Push the repo to GitHub

Login at Streamlit Cloud

Deploy your app directly from GitHub

📸 Demo Screenshot
<img width="965" height="522" alt="image" src="https://github.com/user-attachments/assets/cce2ddb8-03a9-4c6d-8576-7bc1ae12bef2" />

👩‍💻 Author

Masrath Shaik
📧 shaikmasrath1624@gmail.com
