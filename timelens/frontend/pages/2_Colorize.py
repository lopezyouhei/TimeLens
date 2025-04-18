import streamlit as st
import requests

st.title("Image Colorizer")
st.write("Upload a greyscale image to colorize.")

col1, col2 = st.columns([2, 1])

with col1:
    uploaded_file = st.file_uploader(
        "Choose an image to colorize...", 
        type=["jpg", "jpeg", "png", "bmp", "tif", "tiff"]
    )
    button = st.button("Colorize Image")

    if button and uploaded_file:
        with st.spinner("Colorizing..."):
            files = {
                "file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)
            }
            response = requests.post(
                "http://localhost:8000/colorize",
                files=files
            )

            if response.status_code == 200:
                st.image(
                    response.content,
                    caption="Colorized Image",
                    use_container_width=True
                )
                st.download_button(
                    "Download Colorized Image",
                    response.content,
                    f"colorized_{uploaded_file.name}.png"
                )
            else:
                print("Failed to enhance image.")

with col2:
    st.write("Colorize example images:")