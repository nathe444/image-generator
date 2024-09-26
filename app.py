import streamlit as st
import requests
from dotenv import load_dotenv
import os
from PIL import Image
from io import BytesIO
import time

load_dotenv()
hugging_face_api = os.getenv('hugging_face_api')

st.set_page_config(page_title="🖼️ Image Generator", page_icon="🎨", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #544570 0%, #0b1636 100%);
        padding: 20rem;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }

    textarea {
        background-color: #f8e8e8;
        border: 1px solid #e0e0e0;
        padding: 10px;
        border-radius: 10px;
        width: 100%;
        font-size: 16px;
    }

    .stButton button {
        background-color: #6200ea;  
        color: white;
        padding: 10px 20px;
        border-radius: 8px;
        font-size: 18px;
        transition: background-color 0.3s;
    }

    .stButton button:hover {
        background-color: #3700b3;  
    }

    .stImage img {
        margin: 0 auto;
        border-radius: 15px;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);
    }

    h1 {
        color: #ffffff;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
        font-weight: bold;
        font-size: 30px;
        margin-top: 50px;
    }

    </style>
    """, unsafe_allow_html=True
)

st.title("🖼️ Generate Images with 1 click")

prompt = st.text_area("Enter your creative prompt here:", placeholder="Describe the image you'd like to generate...", height=150)

API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
headers = {"Authorization": f"Bearer {hugging_face_api}"}

def generate_image(prompt):
    data = {"inputs": prompt}
    while True:
        response = requests.post(API_URL, headers=headers, json=data)

        if response.status_code == 503:
            st.write(f"Model is loading, waiting for {response.json().get('estimated_time', 60)} seconds...")
            time.sleep(min(response.json().get("estimated_time", 60), 60))  
        elif response.status_code == 200:
            return response
        else:
            st.write(f"Error {response.status_code}: {response.text}")
            return None

if st.button("Generate Image 🎨"):
    if prompt:
        with st.spinner("Generating your image..."):
            response = generate_image(prompt)
            if response:
                image = Image.open(BytesIO(response.content))
                st.image(image, caption="Your AI-Generated Masterpiece", use_column_width=True)
            else:
                st.write("Please enter a prompt.")
    else:
        st.write("Please enter a prompt.")
