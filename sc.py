import streamlit as st
import requests
import random
import time
from PIL import Image

# Initialize session state
if 'previous_query' not in st.session_state:
    st.session_state.previous_query = None

# Constants
GROQ_API_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_TOKEN = "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"
HF_API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
HF_TOKEN = "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"  # Get your free token from huggingface.co

def generate_image_hf(prompt):
    """Generate image using Hugging Face's free inference API"""
    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "inputs": prompt,
        "options": {
            "wait_for_model": True
        }
    }

    try:
        with st.spinner("Generating image..."):
            response = requests.post(HF_API_URL, headers=headers, json=payload)
            if response.status_code == 200:
                return response.content
            else:
                st.error(f"Error: {response.status_code}")
                return None
    except Exception as e:
        st.error(f"Error generating image: {str(e)}")
        return None

def groq_request(prompt, model="llama3-8b-8192"):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_TOKEN}"
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        with st.spinner("Generating story..."):
            response = requests.post(GROQ_API_ENDPOINT, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        st.error(f"Error generating story: {str(e)}")
        return None

def save_story_as_markdown(story, image_descriptions):
    """Save story and image descriptions as markdown"""
    markdown_content = "# Generated Story\n\n"

    paragraphs = story.split("\n\n")
    for i, (paragraph, image_desc) in enumerate(zip(paragraphs, image_descriptions)):
        markdown_content += f"{paragraph}\n\n"
        if image_desc:
            markdown_content += f"*Image {i+1}: {image_desc}*\n\n"

    return markdown_content

def main():
    st.title("Interactive Story Generator")
    st.write("Generate entertaining stories with AI-generated images. Perfect for creative and interactive fun!")

    # Check for HF token
    if not HF_TOKEN:
        st.error("""Please set up your free Hugging Face token:
        1. Go to https://huggingface.co and sign up
        2. Go to https://huggingface.co/settings/tokens
        3. Create a new token
        4. Copy and paste it into the HF_TOKEN variable in the code""")
        return

    # Sidebar for theme selection
    themes = ["Adventure", "Fantasy", "Friendship", "Mystery", "Nature"]
    theme = st.sidebar.selectbox("Select a theme (optional)", [""] + themes)

    # Style selection for images
    art_styles = ["Realistic", "Watercolor", "Oil Painting", "Digital Art", "Anime"]
    art_style = st.sidebar.selectbox("Select art style", art_styles)

    # Image quality settings
    quality_setting = st.sidebar.slider("Image Quality", min_value=1, max_value=3, value=2, 
                                      help="Higher quality takes longer to generate")

    # Main input area
    prompt = st.text_area("Enter your story prompt...", height=100)

    if st.button("Generate Story"):
        if not prompt:
            st.error("Please provide a prompt to generate your story.")
            return

        if not theme:
            theme = random.choice(themes)
            st.info(f"Using random theme: {theme}")

        # Generate story
        story = groq_request(f"Generate an engaging, descriptive, and positive story for the theme '{theme}' with the following prompt: {prompt}")

        if story:
            # Split story into paragraphs
            paragraphs = story.split("\n\n")

            # Determine indices for image generation
            num_images = min(4, len(paragraphs))
            image_indices = sorted(random.sample(range(len(paragraphs)), num_images))

            generated_images = []
            image_descriptions = []

            for i, paragraph in enumerate(paragraphs):
                st.write(paragraph)

                if i in image_indices:
                    # Generate image prompt from paragraph
                    image_prompt = f"Generate a descriptive and visual prompt for this paragraph: {paragraph}"
                    img_prompt_response = groq_request(image_prompt)

                    if img_prompt_response:
                        # Add art style to prompt
                        styled_prompt = f"{img_prompt_response}, {art_style} style, highly detailed, professional quality, sharp focus"

                        # Generate image with retries
                        max_retries = quality_setting
                        for _ in range(max_retries):
                            image_data = generate_image_hf(styled_prompt)
                            if image_data:
                                generated_images.append(image_data)
                                image_descriptions.append(img_prompt_response)
                                st.image(image_data, caption=f"Generated image for paragraph {i+1}")
                                break
                            time.sleep(2)  # Wait before retry

            # Save and offer download
            if generated_images:
                markdown_content = save_story_as_markdown(story, image_descriptions)

                # Offer both markdown and plain text downloads
                st.download_button(
                    label="Download Story as Markdown",
                    data=markdown_content,
                    file_name="Generated_Story.md",
                    mime="text/markdown"
                )

                st.download_button(
                    label="Download Story as Text",
                    data=story,
                    file_name="Generated_Story.txt",
                    mime="text/plain"
                )
            else:
                st.warning("Could not generate images, but your story has been created.")
                st.write(story)
                st.download_button(
                    label="Download Story as Text",
                    data=story,
                    file_name="Generated_Story.txt",
                    mime="text/plain"
                )

if __name__ == "__main__":
    main()
