from pydantic import BaseSettings
from typing import List, Optional
from app.models.pipeline_preset import PipelinePreset

class Settings(BaseSettings):
    app_name: str = "Fastcasso"
    simple_diffusion_model_id: str = "CompVis/stable-diffusion-v1-4"
    simple_diffusion_device:str = "mps"
    safety_check:bool = False
    num_inference_steps:int = 50
    presets: List[PipelinePreset] = (
    [PipelinePreset(model_id="CompVis/stable-diffusion-v1-4", inference_steps=50, preset_id=1),
    PipelinePreset(model_id="runwayml/stable-diffusion-v1-5", inference_steps=50, preset_id=2),]
    )