import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
import joblib

# Generate synthetic dataset
np.random.seed(42)
data = {
    'user_id': np.arange(1, 101),
    'time_spent': np.random.randint(20, 120, 100),
    'quiz_score': np.random.randint(50, 100, 100),
    'preferred_study_time': np.random.choice(['morning', 'afternoon', 'evening'], 100),
    'difficulty_level': np.random.choice(['easy', 'medium', 'hard'], 100),
    'past_performance': np.random.randint(40, 100, 100),
    'study_frequency': np.random.randint(1, 7, 100),
}

df = pd.DataFrame(data)

# Convert categorical features to numerical
study_time_map = {'morning': 0, 'afternoon': 1, 'evening': 2}
difficulty_map = {'easy': 0, 'medium': 1, 'hard': 2}

df['preferred_study_time'] = df['preferred_study_time'].map(study_time_map)
df['difficulty_level'] = df['difficulty_level'].map(difficulty_map)

# Generate target variable
df['weak_area'] = ((df['quiz_score'] < 70) & (df['difficulty_level'] == 2)).astype(int)

# Features and target
X = df.drop(columns=['user_id', 'weak_area'])
y = df['weak_area']

# Feature Scaling
scaler = StandardScaler()
X[['time_spent', 'quiz_score', 'past_performance', 'study_frequency']] = scaler.fit_transform(
    X[['time_spent', 'quiz_score', 'past_performance', 'study_frequency']]
)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "student_scheduler_model.pkl")
print("✅ Model trained and saved as student_scheduler_model.pkl")