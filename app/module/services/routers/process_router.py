from fastapi import APIRouter, Depends, HTTPException
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from schema.request.sample_request import Item
from service.tilt_correction import Orientation


router = APIRouter(
    prefix="/items",
    tags=["items"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.post('/tilt_correction')
async def get_tilt_corrected_image(img:str): 
    image,angle = Orientation(img,0,).re_orient_east()
    print(image)
    print('*********')
    print(angle)


@router.post("/tilt_correction", response_model=TiltInferenceResponse)
async def _run_inference_tilt(request: TiltInferenceRequest):

    return await inference_service.run_ocr_triton_inference(
        request, request_state.state.api_key_name, request_state.state.user_id
    )