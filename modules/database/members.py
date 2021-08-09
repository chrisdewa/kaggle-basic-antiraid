from datetime import datetime
from typing import Optional

from odmantic import Model

from config import KAGGLE_SERVER_ID
from .models import ModelExt

__all__ = (
    'MemberModel',
)


class MemberModel(ModelExt, Model):
    member_id: int
    guild_id: int = KAGGLE_SERVER_ID
    muted_on: Optional[datetime] = None
    unmute_on: Optional[datetime] = None

    class Config:
        collection = 'members'
