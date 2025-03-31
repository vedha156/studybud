
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("student_scheduler_model.pkl")

# Streamlit UI
st.title("🎓 Student Task Scheduling System")
st.header("Enter Your Study Details")

# User input fields
time_spent = st.slider("Time Spent Per Topic (minutes)", min_value=20, max_value=120, value=60)
quiz_score = st.slider("Recent Quiz Score", min_value=50, max_value=100, value=75)
past_performance = st.slider("Past Performance Score", min_value=40, max_value=100, value=70)
study_frequency = st.slider("Study Frequency (sessions per week)", min_value=1, max_value=7, value=4)

preferred_study_time = st.selectbox("Preferred Study Time", ['Morning', 'Afternoon', 'Evening'])
difficulty_level = st.selectbox("Difficulty Level", ['Easy', 'Medium', 'Hard'])

# Convert categorical inputs to numerical values
study_time_map = {'Morning': 0, 'Afternoon': 1, 'Evening': 2}
difficulty_map = {'Easy': 0, 'Medium': 1, 'Hard': 2}

preferred_study_time = study_time_map[preferred_study_time]
difficulty_level = difficulty_map[difficulty_level]

# Prepare input data with correct feature names
input_data = pd.DataFrame([[time_spent, quiz_score, past_performance, study_frequency, preferred_study_time, difficulty_level]],
                          columns=['time_spent', 'quiz_score', 'past_performance', 'study_frequency', 'preferred_study_time', 'difficulty_level'])

# Predict button
if st.button("📊 Predict My Weak Areas"):
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.error("⚠️ Based on your data, you might struggle with certain topics. Consider focusing more on them!")
    else:
        st.success("✅ Great job! You seem to be on track with your studies!")
*/
