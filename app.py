import re
import streamlit as st
from groq import Groq
import os

# Read key from Streamlit Secrets (deployment) or env (local)
api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

st.title("ClariCode - Your AI Code Explanation Tool")
st.write("Paste your code snippet below, and I'll explain how it works, what language it uses, and potential use cases.")

# Input area
user_input = st.text_area("Enter Your Code Snippet:", height=200)

# Simple heuristic to check if input looks like code
def looks_like_code(text):
    code_patterns = [
        r"\bdef\b", r"\bclass\b", r"\bimport\b", r"#include", r";", r"\{.*\}", r"//", r"function", r"public", r"static"
    ]
    return any(re.search(p, text) for p in code_patterns)

# Button triggers explanation
if st.button("Get Explanation"):
    if user_input.strip():
        if not looks_like_code(user_input):
            st.warning("  Sorry but it looks like you didn't enter code. Please paste a valid code snippet.")
        else:
            with st.spinner("Generating explanation..."):
                try:
                    completion = client.chat.completions.create(
                        model="llama3-8b-8192",
                        messages=[
                            {
                                "role": "system",
                                "content": (
                                    "You are ClariCode, an expert AI code explainer. "
                                    "For the given input, provide a comprehensive explanation of the code including:\n"
                                    "- Language used\n"
                                    "- Working mechanism\n"
                                    "- Key components\n"
                                    "- Real-world use cases\n"
                                )
                            },
                            {"role": "user", "content": user_input}
                        ],
                        temperature=0.7,
                        max_tokens=1230,
                        top_p=1,
                        stream=True,
                    )

                    # Collect streaming chunks
                    explanation = ""
                    for chunk in completion:
                        content = chunk.choices[0].delta.content
                        if content:
                            explanation += content

                    st.subheader("📘 Code Explanation")
                    st.write(explanation)

                except Exception as e:
                    st.error(f"An error occurred: {e}")
    else:
        st.warning("⚠️ Please enter a code snippet before clicking the button.")


