"""
Config module: contains constants, presets, and environment variable loading.
"""

import os
from dotenv import load_dotenv

load_dotenv()  
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Pollinations.ai API Key 
TXTTOIMG_API = os.getenv("txttoimg_api")
# OPEN_ROUTER_API=os.getenv("Open_Router_Api")


STYLE_PRESETS = {
    "Photorealistic": "ultra-realistic, high detail, 35mm, cinematic lighting, photorealistic",
    "Digital Painting": "digital painting, brush strokes, rich color palette, cinematic lighting",
    "Watercolor": "soft watercolor painting, delicate textures, pastel tones, high resolution",
    "Low-Poly Art": "low-poly stylized art, geometric shapes, minimalistic shading",
    "Cyberpunk": "cyberpunk, neon lights, reflective surfaces, high contrast, futuristic cityscape",
    "Fantasy Illustration": "epic fantasy illustration, intricate details, dramatic lighting, magical atmosphere",
    "Anime": "anime style, clean lineart, vibrant colors, dramatic composition",
    "Retro VHS": "retro VHS aesthetic, film grain, chromatic aberration, muted color grading"
}

DEFAULT_NEGATIVE_PROMPT = (
    "low quality, blurry, deformed, watermark, text, signature, extra limbs, "
    "oversaturated, underexposed, jpeg artifacts, poorly drawn"
)

QUALITY_PRESETS = {
    "Draft (fast)": {"num_inference_steps": 12, "guidance_scale": 6.0},
    "Standard": {"num_inference_steps": 28, "guidance_scale": 7.5},
    "High (slow)": {"num_inference_steps": 50, "guidance_scale": 8.5},
}

MAX_IMAGES_PER_REQUEST = 4
