import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(page_title="Fancy BMI Calculator", layout="centered")

# Background animation + custom style
st.markdown("""
    <style>
    body {
        background: linear-gradient(-45deg, #fbc2eb, #a6c1ee, #fad0c4, #ffd3a5);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }

    @keyframes gradient {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .stApp {
        background-color: transparent;
        font-family: 'Segoe UI', sans-serif;
    }

    .title {
        text-align: center;
        font-size: 3em;
        color: #2c3e50;
        font-weight: 700;
        margin-top: 10px;
        margin-bottom: 30px;
    }

    .bmi-result {
        font-size: 1.3em;
        text-align: center;
        margin-top: 20px;
    }

    .circle-wrapper {
        display: flex;
        justify-content: center;
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">💪 Fancy BMI Calculator 💫</div>', unsafe_allow_html=True)

# Input section
col1, col2 = st.columns(2)
with col1:
    height = st.number_input("📏 Height (meters):", min_value=0.5, max_value=2.5, step=0.01)
with col2:
    weight = st.number_input("⚖️ Weight (kg):", min_value=10.0, max_value=300.0, step=0.1)

# Function to get category and emoji
def get_category_emoji(bmi: float):
    if bmi < 18.5:
        return "Underweight", "😟", "#3498db"
    elif 18.5 <= bmi < 25:
        return "Normal", "😃", "#2ecc71"
    elif 25 <= bmi < 30:
        return "Overweight", "😐", "#f1c40f"
    else:
        return "Obese", "⚠️", "#e74c3c"

# Calculate BMI
if st.button("✨ Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        category, emoji, color = get_category_emoji(bmi)

        # Circular progress bar using HTML/CSS
        percent = min(int(bmi * 3), 100)

        st.markdown(f"""
        <div class="circle-wrapper">
            <svg width="160" height="160">
              <circle cx="80" cy="80" r="70" stroke="#eee" stroke-width="15" fill="none" />
              <circle cx="80" cy="80" r="70" stroke="{color}" stroke-width="15"
                fill="none" stroke-dasharray="{percent * 4.4} 440" stroke-linecap="round"
                transform="rotate(-90 80 80)" />
              <text x="50%" y="50%" text-anchor="middle" dy=".3em" font-size="24" fill="{color}" font-weight="bold">
                {bmi:.1f}
              </text>
            </svg>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="bmi-result">
            Your BMI Category: <strong>{category}</strong> {emoji} <br>
            <small style="color:gray">Normal range: 18.5 - 24.9</small>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Please enter a valid height.")
