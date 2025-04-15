import streamlit as st
from PIL import Image
import pytesseract
import cv2
import numpy as np

st.set_page_config(page_title="Image to Text OCR", layout="centered")

st.title("📄 Image to Text OCR App")
st.write("Upload an image and extract text using Tesseract OCR.")

uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Convert to OpenCV format
    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Optional: Convert to grayscale and threshold for better accuracy
    gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
    processed = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # OCR with pytesseract
    text = pytesseract.image_to_string(processed)

    st.subheader("📝 Extracted Text")
    st.text_area("OCR Output", text, height=300)
