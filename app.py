"""
Streamlit web app for the IMDB sentiment classifier.
Run locally with: streamlit run app.py
"""

import re
import joblib
import streamlit as st

st.set_page_config(page_title="Movie Review Sentiment Analyzer", page_icon="🎬")


def clean_text(text: str) -> str:
    text = re.sub(r"<br\s*/?>", " ", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text.lower()


@st.cache_resource
def load_model():
    model = joblib.load("sentiment_model.pkl")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")
    return model, vectorizer


model, vectorizer = load_model()

st.title("🎬 Movie Review Sentiment Analyzer")
st.write(
    "Type a movie review below and the model will predict whether it's "
    "positive or negative. Trained on 40,000 IMDB reviews using TF-IDF + Logistic Regression."
)

user_input = st.text_area(
    "Your review:",
    placeholder="e.g. This film was a total waste of time...",
    height=120,
)

if st.button("Analyze Sentiment", type="primary"):
    if not user_input.strip():
        st.warning("Please enter some text first.")
    else:
        cleaned = clean_text(user_input)
        vec = vectorizer.transform([cleaned])
        prediction = model.predict(vec)[0]
        proba = model.predict_proba(vec)[0]
        classes = model.classes_
        confidence = proba.max()

        if prediction == "positive":
            st.success(f"**Positive** 😀 ({confidence:.1%} confidence)")
        else:
            st.error(f"**Negative** 😞 ({confidence:.1%} confidence)")

        st.write("Confidence breakdown:")
        st.bar_chart(
            {"Sentiment": list(classes), "Confidence": list(proba)},
            x="Sentiment",
            y="Confidence",
        )

st.divider()
st.caption(
    "Note: this model is trained on movie reviews and uses simple word-based "
    "features, so it can struggle with sarcasm, negation, or mixed opinions."
)