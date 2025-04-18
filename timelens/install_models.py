import os
import urllib.request

from backend import MODEL_PATH

def download_model(url: str, output_folder: str = MODEL_PATH) -> None:
    os.makedirs(output_folder, exist_ok=True)
    filename = url.split("/")[-1]
    output_path = os.path.join(output_folder, filename)

    if not os.path.exists(output_path):
        urllib.request.urlretrieve(url, output_path)

if __name__ == "__main__":
    realesrgan_urls = [
        "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth",
        "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.1/RealESRGAN_x2plus.pth",
        "https://huggingface.co/spensercai/DeOldify/resolve/main/ColorizeStable_gen.pth"
    ]
    for model_url in realesrgan_urls:
        download_model(model_url)
