import streamlit as st
import requests
import os

frontend_path = os.path.dirname(os.path.dirname(__file__))
assets_path = os.path.join(frontend_path, "assets")

st.title("Image Colorizer")


col1, col2 = st.columns([1.3, 1])

with col1:
    st.write("Upload a greyscale image to colorize.")
    uploaded_file = st.file_uploader(
        "Choose an image to colorize...", 
        type=["jpg", "jpeg", "png", "bmp", "tif", "tiff"]
    )
    button = st.button("Colorize Image")

    if button and uploaded_file:
        filename = uploaded_file.name
        filename = filename.split(".")[0]
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
                    f"colorized_{filename}.png"
                )
            else:
                print("Failed to enhance image.")

with col2:
    subcol1, subcol2 = st.columns([1, 1])
    with subcol1:
        st.subheader("Original")
        st.image(os.path.join(assets_path, "colorize/race_car.jpg"), use_container_width=True)
    with subcol2:
        st.subheader("Colorized")
        st.image(os.path.join(assets_path, "colorize/colorized_race_car.png"), use_container_width=True)