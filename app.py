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

# Custom CSS styling for the app
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #544570 0%, #0b1636 100%);  # Background gradient
    }

    .block-container {
        padding: 2rem;  # Padding for the main container
    }

    textarea {
        background-color: #f8e8e8;  # Background color for text area
        border: 1px solid #e0e0e0;  # Border style for text area
        padding: 10px;  # Padding inside the text area
        border-radius: 10px;  # Rounded corners for text area
        width: 100%;  # Full width for text area
        font-size: 16px;  # Font size for text area
    }

    .stButton button {
        background-color: #6200ea;  # Button background color
        color: white;  # Button text color
        padding: 10px 20px;  # Padding for buttons
        border-radius: 8px;  # Rounded corners for buttons
        font-size: 18px;  # Font size for button text
        transition: background-color 0.3s;  # Transition effect for hover
    }

    .stButton button:hover {
        background-color: #3700b3;  # Button background color on hover
    }

    .stImage img {
        margin: 0 auto;  # Center the image
        border-radius: 15px;  # Rounded corners for images
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);  # Shadow effect for images
    }

    h1 {
        color: #ffffff;  # Header text color
        text-align: center;  # Center header text
        font-family: 'Helvetica', sans-serif;  # Font family for header
        font-weight: bold;  # Bold font for header
        font-size: 30px;  # Font size for header
        margin-top: 20px;  # Margin above header
    }

    @media (max-width: 768px) {
        .block-container {
            padding: 10rem 0rem;  # Responsive padding for small screens
        }
        h1 {
            font-size: 20px;  # Responsive font size for header
        }
        textarea {
            font-size: 8px;  # Responsive font size for text area
        }
        .stButton button {
            font-size: 12px;  # Responsive font size for button
            padding: 8px 16px;  # Responsive padding for button
        }
    }
    </style>
    """, unsafe_allow_html=True
)

st.title("🖼️ Generate Images with a click")

prompt = st.text_area("Enter your creative prompt here:", placeholder="Describe the image you'd like to generate...", height=150)

# Add a select box for the user to choose an API
api_option = st.selectbox(
    "Select an API model for image generation:",
    [
        "FLUX.1-dev",        # API 1
        "How2Draw",          # API 2
        "Stable Diffusion v1.4"  # API 3
    ]
)

# API URLs for different models
API_URLS = {
    "FLUX.1-dev": "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev",
    "How2Draw": "https://api-inference.huggingface.co/models/glif/how2draw",
    "Stable Diffusion v1.4": "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4",
}

# Set the API URL based on the user's selection
API_URL = API_URLS[api_option]
headers = {"Authorization": f"Bearer {hugging_face_api}"}  

# Function to generate an image based on the prompt
def generate_image(prompt):
    data = {"inputs": prompt}  
    while True:
        response = requests.post(API_URL, headers=headers, json=data) 
        if response.status_code == 503:  # If the model is loading
            st.write(f"Model is loading, waiting for {response.json().get('estimated_time', 60)} seconds...")  # Notify user about loading time
            time.sleep(min(response.json().get("estimated_time", 60), 60))  # Wait for the specified time
        elif response.status_code == 200:  # If the response is successful
            return response  # Return the response
        else:
            st.write(f"Error {response.status_code}: {response.text}")  # Display error message
            return None  # Return None if there's an error

# Button for generating the image
if st.button("Generate Image 🎨"):
    if prompt:  
        with st.spinner("Generating your image..."):  
            response = generate_image(prompt)  
            if response:
                image = Image.open(BytesIO(response.content))  # Open the image from response
                st.image(image, caption="Your AI-Generated Masterpiece", use_column_width=True)  # Display the generated image

                # Prepare image for download
                buffered = BytesIO()
                image.save(buffered, format="png")  # Save the image to a BytesIO buffer
                img_bytes = buffered.getvalue()  # Get byte value of the image

                
                st.download_button(
                    label="Download Image",
                    data=img_bytes,  # Image data
                    file_name="image.png",  # Default file name for download
                    mime="image/png",  # MIME type for PNG image
                )
    else:
        st.write("Please enter a prompt.")  # Prompt user to enter a prompt if empty
