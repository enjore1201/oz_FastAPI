from pydantic import BaseModel

from app.dtos.frozen_config import FROZEN_CONFIG

# from app.tortoise_models.base_model import BaseModel


class GetMeetingResponse(BaseModel):
    model_config = FROZEN_CONFIG

    url_code: str
