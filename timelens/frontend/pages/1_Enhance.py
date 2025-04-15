import streamlit as st
import requests

st.title("Image Enhancer")
st.write("Upload an image and select a resolution (2x or 4x).")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
scale_option = st.radio("Select scale", ["x2", "x4"])
button = st.button("Enhance Image")

if button and uploaded_file and scale_option:
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
                "enhanced_image.png"
            )
        else:
            print("Failed to enhance image.")