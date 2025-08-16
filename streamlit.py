import streamlit as st
from PIL import Image

# App title
st.set_page_config(page_title="AgriVision AI", page_icon="🌱", layout="wide")

st.title("🌱 AgriVision AI")
st.write("Making farming smarter with AI and satellite insights.")

# Sidebar
st.sidebar.header("Navigation")
option = st.sidebar.radio("Go to:", ["Home", "Upload Image", "About"])

# Home Page
if option == "Home":
    st.subheader("🚀 Welcome to AgriVision AI")
    st.write("""
    AgriVision AI helps farmers and researchers identify crops and detect early health issues 
    using satellite imagery and AI.  
    With a Gen-AI assistant, it provides **simple, actionable advice in multiple languages**.
    """)

# Upload Image Page
elif option == "Upload Image":
    st.subheader("📷 Upload a Crop Image")
    uploaded_file = st.file_uploader("Upload a field or crop image", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Placeholder for AI result
        st.success("✅ AI Prediction: This looks like **Wheat** 🌾")
        st.info("💡 Advice: Ensure proper irrigation and check for leaf rust symptoms.")

# About Page
elif option == "About":
    st.subheader("ℹ️ About AgriVision AI")
    st.write("""
    - Built by college students for the **India AI Impact Hackathon**  
    - Combines **Satellite Imagery + AI + Gen-AI**  
    - Supports **multilingual farmer advisory**  
    - Goal: Make **precision agriculture accessible** for everyone  
    """)

st.markdown("---")
st.caption("Made with ❤️ by Students")
