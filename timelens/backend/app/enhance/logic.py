from basicsr.archs.rrdbnet_arch import RRDBNet
import cv2
from fastapi import UploadFile
from functools import lru_cache
import numpy as np
import os
from realesrgan import RealESRGANer
import sys
import torch

backend_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(backend_path)
from app import MODEL_PATH
print(MODEL_PATH)

# lazy load models to avoid loading multiple models into (GPU) memory
@lru_cache(maxsize=1)
def load_model(scale:str) -> RealESRGANer:
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    half = device.type == "cuda"
    
    if scale == "x2":
        model_arch = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64,
                         num_block=23, num_grow_ch=32, scale=2)
        return RealESRGANer(
            scale=2,
            model_path=os.path.join(MODEL_PATH, "RealESRGAN_x2plus.pth"),
            model=model_arch,
            device=device,
            half=half
        )
    elif scale == "x4":
        model_arch = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64,
                         num_block=23, num_grow_ch=32, scale=4)
        return RealESRGANer(
            scale=4,
            model_path=os.path.join(MODEL_PATH, "RealESRGAN_x4plus.pth"),
            model=model_arch,
            device=device,
            half=half
        )
    else:
        raise ValueError("Invalid scale selected")

async def enhance_image(file: UploadFile, scale: str) -> np.ndarray:
    image_data = await file.read()
    np_img = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)

    model = load_model(scale)
    output, _ = model.enhance(np_img)

    return output