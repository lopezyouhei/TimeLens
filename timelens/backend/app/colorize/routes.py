import cv2
from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import Response
from io import BytesIO

from app.colorize.logic import colorize_image

router = APIRouter()

@router.post("/")
async def colorize_endpoint(file: UploadFile = File(...)) -> Response:
    # check whether the file is an image
    if not file.content_type.startswith("image/"):
        return Response(content="File is not an image", status_code=400)
    try:
        colorized_image = await colorize_image(file)
        
        # convert PIL Image to bytes
        buffer = BytesIO()
        colorized_image.save(buffer, format="PNG")
        buffer.seek(0)
 
        return Response(content=buffer.getvalue(), media_type="image/png")
    except Exception as e:
        return Response(content=str(e), status_code=500)