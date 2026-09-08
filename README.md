# IMDB Sentiment Analyzer — Streamlit Deployment

## Project Structure

```text
imdb-sentiment-streamlit/
├── app.py
├── sentiment_model.pkl
├── tfidf_vectorizer.pkl
└── requirements.txt
```

## 1. Requirements

Create a file named `requirements.txt`:

```text
streamlit
scikit-learn
joblib
```

## 2. Test the App Locally

Open Command Prompt or PowerShell in the project folder:

```bash
cd path/to/imdb-sentiment-streamlit
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The application should open in your browser.

## 3. Create a GitHub Repository

1. Go to GitHub: https://github.com/
2. Sign in to your account.
3. Click **New repository**.
4. Give the repository a name, for example:

```text
imdb-sentiment-streamlit
```

5. Select **Public** if you want a public repository.
6. Click **Create repository**.

## 4. Upload the Project Files

Upload these files to the GitHub repository:

```text
app.py
sentiment_model.pkl
tfidf_vectorizer.pkl
requirements.txt
```

The filenames must match the names used by `app.py`:

```text
sentiment_model.pkl
tfidf_vectorizer.pkl
```

## 5. Deploy with Streamlit Community Cloud

1. Open Streamlit Community Cloud:
   https://share.streamlit.io/
2. Sign in with GitHub.
3. Click **Create app**.
4. Select your GitHub repository.
5. Select the `main` branch.
6. Set the main file path to:

```text
app.py
```

7. Click **Deploy**.

Streamlit will install the packages from `requirements.txt` and run `app.py`.

## 6. Final Project Flow

```text
GitHub Repository
       |
       v
Streamlit Community Cloud
       |
       v
       app.py
       |
       v
Load sentiment_model.pkl
       +
Load tfidf_vectorizer.pkl
       |
       v
User enters movie review
       |
       v
Clean the text
       |
       v
TF-IDF transformation
       |
       v
Sentiment model prediction
       |
       v
Positive / Negative
       |
       v
Confidence score
```

## Important

Do not upload passwords, API keys, private credentials, or other secrets to GitHub.

Make sure the two `.pkl` files are available in the repository because the application loads them directly.
