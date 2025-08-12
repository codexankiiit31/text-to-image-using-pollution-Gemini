"""
Image generator module using Pollinations.ai API for text-to-image generation.
Generates images from an enhanced prompt.
"""
import os
import requests
from PIL import Image
from io import BytesIO
from typing import List
import urllib.parse
from config import TXTTOIMG_API
# from config import OPEN_ROUTER_API

def generate_images(prompt: str, num_images: int = 1, image_ratio: str = "1:1") -> List[Image.Image]:
    """
    Generate images from prompt using Pollinations.ai API.
    Args:
        prompt (str): The enhanced prompt text.
        num_images (int): Number of images to generate (max 4 recommended).
        image_ratio (str): Desired aspect ratio ("1:1", "9:16", "16:9").
    Returns:
        List[PIL.Image.Image]: List of generated PIL Image objects.
    Raises:
        RuntimeError: If the API call fails or returns an error.
    """
    if num_images < 1 or num_images > 4:
        raise ValueError("num_images must be between 1 and 4.")
    
    ratio_map = {
        "1:1": (512, 512),
        "9:16": (576, 1024),  # portrait
        "16:9": (1024, 576)   # landscape
    }
    width, height = ratio_map.get(image_ratio, (512, 512))

    images = []
 # Generate images one by one
    for i in range(num_images):
        try:
            # Pollinations.ai API endpoint
            encoded_prompt = urllib.parse.quote(prompt)
            api_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
            
            # Add parameters for better quality
            params = {
                "width": 512,
                "height": 512,
                "seed": i,  # Different seed for each image
                "model": "flux",  # Use flux model for better quality
                "enhance": "true"  # Auto-enhance the prompt
            }
            
            # Add API key if available (Pollinations.ai also works without key)
            headers = {}
            if TXTTOIMG_API:
                headers = {"Authorization": f"Bearer {TXTTOIMG_API}"}
            
            # Make request with parameters
            full_url = f"{api_url}?" + "&".join([f"{k}={v}" for k, v in params.items()])
            response = requests.get(full_url, headers=headers, timeout=30)
            
            if response.status_code != 200:
                raise RuntimeError(f"API error {response.status_code}: {response.text}")
            
            # Convert response to image
            img = Image.open(BytesIO(response.content)).convert("RGB")
            images.append(img)
            
        except Exception as e:
            raise RuntimeError(f"Error generating image {i+1}: {str(e)}")
    
    return images
