import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
import joblib

# Load data
df = pd.read_csv("graded_samples.csv")

# Create pipeline
pipe = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=20000)),
    ("reg", Ridge(alpha=1.0))
])

# Train
pipe.fit(df["text"], df["score"])

# Save model
joblib.dump(pipe, "grade_model.pkl")

print("Model trained and saved!")