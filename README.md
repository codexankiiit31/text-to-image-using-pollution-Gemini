# 🎨 AI Text-to-Image Generator with Prompt Enhancement

A powerful and intuitive web application that transforms simple text ideas into stunning, high-quality images. This project uses a sophisticated two-step AI pipeline: **Google Gemini** enhances your basic prompt into a detailed, artistic description, and then **Pollinations.ai** generates a beautiful image based on that enhanced prompt.

## ✨ Features

* **Smart Prompt Enhancement**: Leverages Google Gemini to automatically enrich simple user prompts with cinematic and artistic details.
* **High-Quality Image Generation**: Utilizes the Pollinations.ai API to produce visually appealing images.
* **Rich Style Presets**: Choose from a variety of styles, including Photorealistic, Anime, Watercolor, and Cyberpunk.
* **Customizable Output**: Control the number of images, quality level, and aspect ratio (1:1, 16:9, 9:16).
* **Intuitive Web Interface**: Built with Streamlit for a clean, fast, and user-friendly experience.
* **Easy to Download**: Instantly download your generated creations with a single click.

---

## ⚙️ How It Works

The application follows a simple yet powerful two-stage process to ensure the highest quality output from a basic input.

`User Input (e.g., "a cat in a library")`
➔ `🤖 Step 1: Gemini Prompt Enhancer` ➔ `Enhanced Prompt (e.g., "A cinematic, photorealistic shot of a fluffy calico cat...")`
➔ `🎨 Step 2: Pollinations.ai Image Generator` ➔ `🖼️ Final Image Output`

1.  **Prompt Enhancement**: The initial prompt, along with the selected style and quality settings, is sent to a Google Gemini model via LangChain. Gemini acts as an expert "prompt engineer," expanding the simple idea into a rich, descriptive paragraph suitable for an advanced image model.
2.  **Image Generation**: The newly enhanced prompt is then passed to the Pollinations.ai API, which renders the final image(s) based on this detailed description.

---

## 🛠️ Tech Stack

* **Backend & AI Orchestration**: Python
* **Web Framework**: Streamlit
* **Prompt Enhancement**: Google Gemini (`gemini-1.5-flash`)
* **AI Framework**: LangChain
* **Image Generation**: Pollinations.ai API
* **Environment Management**: `dotenv`

---

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

* Python 3.9 or higher
* A Git client

### 1. Clone the Repository

First, clone the project repository to your local machine.
``bash
git clone [https://github.com/codexankiiit31/text-to-image-using-pollution-Gemini.git]
cd text-to-image-using-pollution-Gemini
``bash

### 2. Create Virtual Enviroment

conda create -p text2img
conda activate text2img/

### 3. Create Requirements.txt
 pip install -r requirements.txt

### 4. Set Up Enviroments
 .env file
 Get your API key from Google AI Studio ([https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey))
GEMINI_API_KEY="YOUR_GOOGLE_GEMINI_API_KEY"

 Pollinations.ai API key (Optional, but recommended for better performance)
TXTTOIMG_API="YOUR_POLLINATIONS_API_KEY"
### 5.Run the Application
streamlit run app.py
