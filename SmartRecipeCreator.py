import streamlit as st
from openai import OpenAI

# --- Streamlit Page Configuration ---
st.set_page_config(page_title="Bhande's Kitchen", layout="centered", initial_sidebar_state="expanded")

# --- Custom CSS Styling for an exciting, fun & mobile-friendly UI ---
st.markdown("""
    <style>
    /* Global Background Gradient & Font */
    body {
        background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Center title text */
    .css-18e3th9 { 
        text-align: center;
    }
    /* App Title and Subtitle Styling */
    .app-title {
        font-size: 3rem;
        font-weight: 700;
        color: #ffffff;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        margin-bottom: 0.3em;
    }
    .app-subtitle {
        font-size: 1.5rem;
        color: #ffffff;
        text-align: center;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
        margin-bottom: 1.5em;
    }
    /* Input Field Styling */
    .stTextInput > div > div > input, .stTextArea > div > textarea, .stSelectbox > div > div > div {
        border-radius: 8px;
        padding: 10px;
        border: 1px solid #cccccc;
        font-size: 1rem;
    }
    /* Button Styling */
    div.stButton > button {
        background-color: #ff4b4b;
        color: #ffffff;
        border-radius: 12px;
        padding: 12px 24px;
        border: none;
        font-size: 1.1rem;
        font-weight: 600;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
        transition: transform 0.2s;
    }
    div.stButton > button:hover {
        transform: scale(1.05);
    }
    /* Recipe Card Styling */
    .recipe-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        animation: fadeIn 1s ease-in-out;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    /* Header Image Styling */
    .header-img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 30%;
        border-radius: 50%;
        border: 5px solid #fff;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Optional Header Image (Replace the URL with your own logo/image if desired) ---
header_image_url = "https://www.gffoodservice.com.au/content/uploads/2019/08/culinary_terms-hero-1-@2x-1.jpg"  # Placeholder image URL
st.markdown(f'<img src="{header_image_url}" class="header-img">', unsafe_allow_html=True)

# --- App Title & Subtitle ---
st.markdown("<h1 class='app-title'>Bhande's Kitchen</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='app-subtitle'>Your AI-Powered Recipe Generator</h2>", unsafe_allow_html=True)
st.write("Enter the ingredients you have and select your desired cuisine to generate a complete, creative, and fun recipe!")

# --- Input Fields ---
openai_api_key = st.text_input("Enter your OpenAI API key:", type="password")
ingredients = st.text_area("Enter the ingredients you have (comma-separated):")
cuisine_options = [
    "Italian", "Chinese", "Indian", "Mexican", "French",
    "Japanese", "Mediterranean", "American", "Thai", "Other"
]
cuisine = st.selectbox("Select your desired cuisine:", cuisine_options)

# --- Function to Query OpenAI's Chat API ---
def generate_recipe(prompt, api_key):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4",  # Change to the model you prefer (gpt-4-turbo or gpt-3.5-turbo)
        messages=[
            {"role": "system", "content": "You are an expert chef providing detailed and engaging recipes."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=600,
    )
    return response.choices[0].message.content.strip()

# --- Button Click Event to Generate Recipe ---
if st.button("Generate Recipe"):
    if not openai_api_key:
        st.error("Please provide your OpenAI API key.")
    elif not ingredients:
        st.error("Please enter the ingredients.")
    else:
        with st.spinner("Cooking up your delicious recipe..."):
            prompt = (
                f"You are a professional chef. Based on the following ingredients: {ingredients}, "
                f"and the cuisine: {cuisine}, provide a complete recipe. Include a title, a list of ingredients, "
                f"and detailed step-by-step cooking instructions. Make it creative, fun, and engaging."
            )
            st.markdown("### Prompt sent to OpenAI:")
            st.code(prompt, language="markdown")
            try:
                recipe = generate_recipe(prompt, openai_api_key)
                st.markdown("### Your Generated Recipe:")
                st.markdown(f'<div class="recipe-card">{recipe}</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"An error occurred: {e}")
