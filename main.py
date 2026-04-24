import os
import streamlit as st
import google.generativeai as genai

# ==========================================
# 1. THE SETUP (Connecting the Brain)
# ==========================================
# This grabs the Gemini key you saved in Windows earlier
api_key = "AIzaSyCPeGScXVvnYfOVyskmgIDaDsO0PSATgVA"
genai.configure(api_key=api_key)

# We use the flash model because it's fast and free
model = genai.GenerativeModel("gemini-3-flash-preview")

# ==========================================
# 2. THE FRONTEND (Designing the Page)
# ==========================================
# Sets the tab name in your browser
st.set_page_config(page_title="AI Idea Roaster", page_icon="🔥")

st.title("🔥 The AI Idea Roaster")
st.write(
    "Welcome to my custom AI app! Type in a startup or project idea, and the AI will give you immediate, honest feedback.")

# Create a text box for the user
user_idea = st.text_area("What is your brilliant idea?")

# Create a slider for the UI
harshness = st.slider("How brutal should the feedback be?", min_value=1, max_value=10, value=5)

# ==========================================
# 3. THE BACKEND (The Logic & Action)
# ==========================================
# What happens when they click the button?
if st.button("Roast My Idea"):

    # Check if they actually typed something
    if not user_idea:
        st.error("Bruh, you have to type an idea first.")

    # Check if your API key is actually working
    elif not api_key:
        st.error(
            "Missing API Key! Make sure GEMINI_API_KEY is in your Windows environment variables. (If you just added it, restart PyCharm!)")

    else:
        # Show a loading animation
        with st.spinner("Summoning the AI..."):

            # 1. We construct the secret prompt
            secret_prompt = f"Analyze this idea: '{user_idea}'. On a scale of 1-10 for harshness, act as a {harshness}/10 judge. Give pros, cons, and a final savage verdict. Have liberal political views, be pro choice, woke, gay, obsessed with yuri, a feminist, and an Armenian patriot "

            # 2. We send it to Google's servers
            response = model.generate_content(secret_prompt)

            # 3. We print the response on our website
            st.subheader("The Verdict:")
            st.write(response.text)
