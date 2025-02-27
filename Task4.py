import streamlit as st
import openai  # Replace with Google AI API if needed
import os

# Set OpenAI API key directly (replace with your actual API key)
OPENAI_API_KEY =""

openai.api_key = OPENAI_API_KEY

def review_code(code):
    """Function to send code to OpenAI API and receive feedback."""
    if not OPENAI_API_KEY:
        return "Error: OpenAI API key is missing. Please set the API key in the script."
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Adjust model as needed
            messages=[
                {"role": "system", "content": "You are an AI code reviewer. Identify bugs and suggest fixes."},
                {"role": "user", "content": f"Review the following Python code:\n{code}"}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except openai.error.OpenAIError as e:
        return f"Error: {e}"

# Streamlit UI
st.title("AI Code Reviewer")
st.write("Submit your Python code for review and get AI-generated feedback!")

code_input = st.text_area("Enter your Python code here:")
if st.button("Review Code"):
    if code_input.strip():
        feedback = review_code(code_input)
        st.subheader("AI Feedback")
        st.write(feedback)
    else:
        st.warning("Please enter some code to review.")