from deoldify import device
from deoldify.device_id import DeviceId
from deoldify.visualize import get_stable_image_colorizer
from fastapi import UploadFile
from functools import lru_cache
from io import BytesIO
from pathlib import Path
from PIL import Image
import torch

@lru_cache(maxsize=1)
def get_colorizer():
    # define the root folder where the model is stored
    app_path = Path(__file__).resolve().parent.parent
    return get_stable_image_colorizer(root_folder=app_path)

async def colorize_image(file: UploadFile) -> Image:
    image_data = await file.read()
    pil_img = Image.open(BytesIO(image_data)).convert("RGB")
    model = get_colorizer()
    colorized_image = model.filter.filter(pil_img, pil_img)

    return colorized_image
