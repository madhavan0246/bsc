import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# 1. Load dataset
df = pd.read_csv(r"C:\Users\Madhavan\Documents\bsc\backend\Barriers to Continuing Sports .csv")

# 2. Clean column names (important!)
df.columns = df.columns.str.strip()

print("Cleaned Columns:", df.columns.tolist())

# 3. Select features & target
X = df[[
    "What is your age group?",
    "What gender do you identify as?",
    "Current Status",
    "Which area do you belong to?",
    "Which sport(s) have you played?",
    "How long did you play sports (even casually or in school/college teams)?",
    "At what level did you play sports?"
]]

y = df["Did you ever think of continuing sports seriously or professionally?"]

# 4. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 5. Preprocessing
categorical_features = X.columns.tolist()
preprocessor = ColumnTransformer(
    transformers=[("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)]
)

# 6. Build pipeline
clf = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(n_estimators=100, random_state=42))
])

# 7. Train
clf.fit(X_train, y_train)

# 8. Evaluate
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 9. Save model
joblib.dump(clf, "model.pkl")
print("✅ Model saved as model.pkl")
