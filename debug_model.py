import joblib

try:
    model = joblib.load("student_scheduler_model.pkl")
    print("✅ Model loaded successfully!")
except ModuleNotFoundError as e:
    print(f"❌ Missing module: {e.name}")
except Exception as e:
    print(f"⚠️ Other error: {e}")
