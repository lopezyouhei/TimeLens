import cv2
from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import Response
from app.enhance.logic import enhance_image

router = APIRouter()

@router.post("/")
async def enhance_endpoint(file: UploadFile = File(...), scale: str = Form(...)) -> Response:
    # check whether the file is an image
    if not file.content_type.startswith("image/"):
        return Response(content="File is not an image", status_code=400)
    try:
        enhanced_image = await enhance_image(file, scale)
        success, encoded_image = cv2.imencode(".png", enhanced_image)
        if not success:
            raise ValueError("Image encoding failed")
        return Response(content=encoded_image.tobytes(), media_type="image/png")
    except Exception as e:
        return Response(content=str(e), status_code=500)
    