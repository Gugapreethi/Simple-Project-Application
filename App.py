import streamlit as st
from openai import OpenAI
client = OpenAI(api_key="sk-xxxx")
st.title("AI Email Generator")
topic = st.text_input("Enter email")
tone = st.selectbox(
    "Select Tone",
    ["Professional", "Friendly", "Formal"]
)

if st.button("Generate Email"):
prompt = f"Write a {tone} email about {topic}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
          {"role": "user", "content": prompt}
        ]
    )
    email = response.choices[0].message.content
    st.write(email)
