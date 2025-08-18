import os
import streamlit as st
from groq import Groq

# Safe key
api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("GROQ_API_KEY is not set. Add it in Streamlit Secrets (cloud) or as an environment variable / .streamlit/secrets.toml (local).")
    st.stop()

client = Groq(api_key=api_key)

st.title("Hey I Am Your AI Explaination Tool ClariCode")
st.write("Provide A Code Snippet,And I Will Explain It With Working Details And Use Cases.")
user_input = st.text_area("Enter Your Code Snippet Here:", height=200)

if st.button("Get Explanation"):
    if user_input.strip():
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {
                    "role": "system",
                    "content": "For the given input give a comprehensive code explanation,working,the language used and use cases. if the input is not a code ask user to give a code and your name is ClariCode"
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            temperature=1,
            max_tokens=1230,
            top_p=1,
            stream=True,
            stop=None,
        )

        explanation = ""
        for chunk in completion:
            explanation += chunk.choices[0].delta.content or ""
        
        st.subheader("Code Explanation")
        st.write(explanation)
    else:

        st.warning("Please enter some code before clicking the button.")
