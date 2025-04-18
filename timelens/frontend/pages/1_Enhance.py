import streamlit as st
import requests
import os

frontend_path = os.path.dirname(os.path.dirname(__file__))
assets_path = os.path.join(frontend_path, "assets")

st.title("Image Enhancer")

col1, col2 = st.columns([1.3, 1])

with col1:
    
    st.write("Upload an image and select a resolution (2x or 4x).")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    scale_option = st.radio("Select scale", ["x2", "x4"])
    button = st.button("Enhance Image")

    if button and uploaded_file and scale_option:
        filename = uploaded_file.name
        filename = filename.split(".")[0]
        with st.spinner("Enhancing..."):
            files = {
                "file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)
            }
            data = {"scale": scale_option}
            response = requests.post(
                "http://localhost:8000/enhance", 
                files=files,
                data=data
            )

            if response.status_code == 200:
                st.image(
                    response.content, 
                    caption="Enhanced Image", 
                    use_container_width=True
                )
                st.download_button(
                    "Download Enhanced Image", 
                    response.content, 
                    f"enhanced_{scale_option}_{filename}.png"
                )
            else:
                print("Failed to enhance image.")

with col2:
    subcol1, subcol2, subcol3 = st.columns([1, 1, 1])
    with subcol1:
        st.subheader("Original")
        st.image(os.path.join(assets_path, "enhance/dog.jpg"), use_container_width=True)
    with subcol2:
        st.subheader("Enhanced 2x")
        st.image(os.path.join(assets_path, "enhance/enhanced_x2_dog.png"), use_container_width=True)
    with subcol3:
        st.subheader("Enhanced 4x")
        st.image(os.path.join(assets_path, "enhance/enhanced_x4_dog.png"), use_container_width=True)
