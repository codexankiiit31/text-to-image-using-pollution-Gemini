"""
Streamlit UI application for text-to-image generation with prompt enhancement.
Uses Gemini for prompt enhancement and Pollinations.ai for image generation.
"""
import streamlit as st
from prompt_enhancer import enhance_prompt
from image_generator import generate_images
from config import STYLE_PRESETS, QUALITY_PRESETS
from io import BytesIO

st.set_page_config(page_title="AI Text-to-Image Generator", layout="wide", page_icon="🎨")

# Enhanced dark mode style
dark_mode_css = """
<style>
body {
    background-color: #0e1117;
    color: #e6e6e6;
}
section.main {
    background-color: #12181b;
    padding: 1rem 2rem 2rem 2rem;
    border-radius: 10px;
}
.stButton>button {
    background-color: #1f6feb;
    color: white;
    border-radius: 8px;
    height: 3rem;
    width: 100%;
    font-size: 1rem;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background-color: #539bf5;
    color: white;
    transform: translateY(-2px);
}
.sidebar .sidebar-content {
    background-color: #12181b;
}
.stSuccess {
    background-color: #0d5016;
    border: 1px solid #28a745;
}
</style>
"""
st.markdown(dark_mode_css, unsafe_allow_html=True)

st.title("🎨 AI Text-to-Image Generator")
st.markdown("*Powered by Google Gemini + Pollinations.ai*")

with st.sidebar:
    st.header("⚙️ Settings")
    
    # Add info about the services
    st.info("🔹 **Gemini**: Prompt enhancement\n🔹 **Pollinations.ai**: Image generation")
    
    style = st.selectbox("🎨 Select Style Preset", options=list(STYLE_PRESETS.keys()))
    quality = st.selectbox("⭐ Select Quality Level", options=list(QUALITY_PRESETS.keys()))
    num_images = st.slider("📸 Number of images", min_value=1, max_value=4, value=1)
    # Image ratio selector
    image_ratio = st.selectbox("🖼 Select Image Ratio", options=["1:1", "9:16", "16:9"])
    
    # negative_prompt = st.text_area(
    #     "❌ Negative Prompt (optional)", 
    #     help="Elements to avoid in the image",
    #     placeholder="e.g. blurry, low quality, distorted"
    # )

# Main input
user_prompt = st.text_input(
    "✍️ Enter your image prompt", 
    placeholder="e.g. A beautiful sunset over mountains",
    help="Describe what you want to see in the image"
)

if st.button("🚀 Generate Images", type="primary"):
    if not user_prompt.strip():
        st.error("⚠️ Please enter an image prompt to generate.")
    else:
        # Create columns for better layout
        col1, col2 = st.columns([2, 1])
        
        with col1:
            with st.spinner("🤖 Enhancing prompt with Gemini..."):
                enhanced_prompt = enhance_prompt(
                    user_prompt, 
                    STYLE_PRESETS[style], 
                    QUALITY_PRESETS[quality], 
                    # negative_prompt,
                    None,  # hf_token (not used)
                    None   # text_model (not used)
                )
            
            st.markdown("### 📝 Enhanced Prompt")
            st.info(enhanced_prompt)
        
        try:
            with st.spinner(f"🎨 Generating {num_images} image(s) with Pollinations.ai..."):
                images = generate_images(enhanced_prompt, num_images=num_images , image_ratio=image_ratio)
            
            st.success(f"🎉 Successfully generated {len(images)} image(s)!")
            
            # Display images in a grid
            if len(images) == 1:
                st.image(images[0], caption="Generated Image", use_container_width=False)
                
                # Download button
                buf = BytesIO()
                images[0].save(buf, format="PNG")
                byte_im = buf.getvalue()
                
                st.download_button(
                    label="💾 Download Image",
                    data=byte_im,
                    file_name="generated_image.png",
                    mime="image/png",
                    type="secondary"
                )
            else:
                # Multiple images in grid
                cols = st.columns(2 if len(images) <= 2 else 3)
                
                for i, img in enumerate(images):
                    with cols[i % len(cols)]:
                        st.image(img, caption=f"Image {i + 1}", use_container_width=False)
                        
                        # Download button for each image
                        buf = BytesIO()
                        img.save(buf, format="PNG")
                        byte_im = buf.getvalue()
                        
                        st.download_button(
                            label=f"💾 Download {i + 1}",
                            data=byte_im,
                            file_name=f"generated_image_{i + 1}.png",
                            mime="image/png",
                            key=f"download_{i}",
                            type="secondary"
                        )
        
        except Exception as e:
            st.error(f"❌ Error generating images: {e}")
            st.info("💡 Try again or modify your prompt")