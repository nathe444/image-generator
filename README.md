# 🖼️ AI Image Generator with Hugging Face and Streamlit

This project is a simple web-based application that allows users to generate AI-generated images using the Hugging Face Stable Diffusion model. The app is built using **Streamlit** and makes API requests to the **Hugging Face Inference API** to generate images based on user prompts.

## Features
- **Prompt-based image generation**: Users can input a creative prompt to generate a unique AI image.
- **Image download**: Once the image is generated, users can download it directly from the interface.
- **User-friendly interface**: A simple, modern design with responsive elements for a clean user experience.

---

## Requirements

Before running the application, ensure you have the following dependencies installed:

- Python 3.7 or above
- Required Python libraries (see [Installation](#installation))

---

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/nathe444/image-generator.git
    cd image-generator
    ```

2. **Install the required dependencies**:

    You can install the necessary Python packages using the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your Hugging Face API key**:

    - Create a `.env` file in the root directory of your project.
    - Inside the `.env` file, add your Hugging Face API key like this:
    
      ```bash
      hugging_face_api=your_hugging_face_api_key_here
      ```

---

## How to Run

1. **Run the Streamlit app**:

    After setting up everything, you can start the app by running the following command in your terminal:

    ```bash
    streamlit run app.py
    ```

2. **Enter your prompt**:

    Once the app is running, you'll see a text area where you can enter your creative prompt. The app will then generate an AI image based on the text input.

3. **Download the image**:

    After the image is generated, you can download it by clicking the "Download Image" button.

---

## Contact me
If you have any questions, feedback, or want to reach out, feel free to contact me at:

Email: natnaelm552@gmail.com

