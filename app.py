import streamlit as st
from utils.code_debugger import explain_code
from utils.image_gen import generate_image
from utils.ocr import extract_text_from_image
from utils.translator import translate_text
from utils.motivator import get_motivational_quote

st.set_page_config(page_title="TitanAI", layout="wide")
st.title("🤖 TitanAI v1 – Your All-in-One AI Assistant")

feature = st.sidebar.selectbox("Choose a Feature", [
    "Code Debugger", "Image Generator", "OCR", "Translator", "Motivator"
])

if feature == "Code Debugger":
    code = st.text_area("Paste your Python code:")
    if st.button("Explain Code"):
        explanation = explain_code(code)
        st.success(explanation)

elif feature == "Image Generator":
    prompt = st.text_input("Enter an image prompt:")
    if st.button("Generate Image"):
        img_url = generate_image(prompt)
        st.image(img_url)

elif feature == "OCR":
    uploaded_file = st.file_uploader("Upload an image")
    if uploaded_file:
        text = extract_text_from_image(uploaded_file)
        st.text_area("Extracted Text", value=text)

elif feature == "Translator":
    text = st.text_input("Enter text to translate:")
    target = st.selectbox("Target language", ["fr", "es", "de", "hi"])
    if st.button("Translate"):
        translated = translate_text(text, target)
        st.success(translated)

elif feature == "Motivator":
    if st.button("Give me motivation"):
        st.info(get_motivational_quote())