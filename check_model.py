import os

model_path = "student_scheduler_model.pkl"

if os.path.exists(model_path):
    print("✅ Model file found:", model_path)
else:
    print("❌ Model file NOT found! Check the file path.")
