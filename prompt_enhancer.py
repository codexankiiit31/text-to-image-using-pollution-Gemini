""" Handles prompt enhancement using LangChain + Google Gemini. """

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from typing import Optional
from config import GEMINI_API_KEY

# Use Gemini with LangChain
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0.7
)

prompt_template = PromptTemplate(
    input_variables=["user_prompt", "style_desc", "quality_desc", "negative_prompt"],
    template=(
        "You are an expert creative art prompt engineer.\n"
        "Expand the user's short prompt into a cinematic, highly-detailed image prompt.\n"
        "Avoid negative concepts.\n\n"
        "User Prompt: {user_prompt}\n"
        "Style: {style_desc}\n"
        "Quality Notes: {quality_desc}\n"
        "Negative Examples: {negative_prompt}\n\n"
        "Expanded Prompt:"
    )
)

# Create chain using pipe operator
enhancer_chain = prompt_template | llm

def enhance_prompt(user_prompt, style_desc, quality_desc, negative_prompt, hf_token=None, text_model=None):
    """
    Enhance the user's prompt using Gemini with LangChain.
    """
    inputs = {
        "user_prompt": user_prompt,
        "style_desc": style_desc,
        "quality_desc": quality_desc,
        "negative_prompt": negative_prompt
    }
    
    try:
        response = enhancer_chain.invoke(inputs)
        enhanced = response.content if hasattr(response, 'content') else str(response)
        return enhanced.strip()
    except Exception as e:
        # Fallback if API fails
        print(f"Enhancement failed: {e}")
        return f"{user_prompt}, {style_desc}, {quality_desc}, highly detailed, cinematic"