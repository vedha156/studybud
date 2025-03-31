import joblib
import pandas as pd  # Ensure pandas is installed

try:
    model = joblib.load("student_scheduler_model.pkl")  # Load your existing model
    joblib.dump(model, "student_scheduler_model_fixed.pkl")  # Save it properly
    print("✅ Model re-saved successfully as student_scheduler_model_fixed.pkl")
except Exception as e:
    print(f"❌ Error while loading/saving model: {e}")
