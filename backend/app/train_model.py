import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import joblib

# Load the dataset
df = pd.read_csv("../../data/email.csv", encoding="latin1")

# Print the column names to confirm structure (optional)
print("Columns:", df.columns[:10])
print("Total columns:", len(df.columns))

# Features: all columns except 'Email No.' and 'Prediction'
X = df.drop(columns=['Email No.', 'Prediction'])

# Labels: 0 (ham) or 1 (spam) in 'Prediction' column
y = df['Prediction']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Save the trained model (no vectorizer needed, features are already precomputed)
joblib.dump(model, "spam_classifier.pkl")

print("✅ Model trained and saved as spam_classifier.pkl")
