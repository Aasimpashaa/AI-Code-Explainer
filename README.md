# AI Code Explanation Tool (Streamlit + Groq)

ClariCode is a lightweight Streamlit app that explains pasted code snippets using a Groq LLM (Llama 3).
It includes a simple input validator so the app only responds when the input looks like code.

Security first: Don’t hard-code your API key in code or commits. Use environment variables (see below). If you’ve exposed a key already, revoke/rotate it immediately in your Groq dashboard.

--Features

*Explains code: language, working mechanism, key components, and real-world use cases
-Input guard: blocks non-code text with a friendly warning
-Streaming responses for a responsive UX
- Minimal codebase—easy to modify

--Requirements

Python 3.9+
A Groq API key
Packages: streamlit, groq

Usage

Paste a code snippet into the text box.
Click Get Explanation.
If the input doesn’t resemble code, you’ll see a warning:
“Sorry but it looks like you didn't enter code. Please paste a valid code snippet.”

What counts as “code” here?
The heuristic looks for common code cues (e.g., def, class, import, #include, {}, ;, //, function, public, static).
You can refine this behavior in the looks_like_code functio
