import os
import urllib.request

from backend import MODEL_PATH

def download_realesrgan(url: str, output_folder: str = MODEL_PATH) -> None:
    os.makedirs(output_folder, exist_ok=True)
    filename = url.split("/")[-1]
    output_path = os.path.join(output_folder, filename)

    if not os.path.exists(output_path):
        urllib.request.urlretrieve(url, output_path)

if __name__ == "__main__":
    model_url = "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth"
    download_realesrgan(model_url)