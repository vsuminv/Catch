# from django.db import models
#
# from mentor.base_model import BaseModel
#
# from user.models import User
#
# from .room import Room
from django.db import models

from mentor.base_model import BaseModel
from mentor.room import Room
from user.models import User


class RoomJoin(BaseModel):
    user_id = models.CharField(max_length=20)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="roomJoin", db_column="user_user_id")
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="roomJoin", db_column="room_id")

    class Meta:
        db_table = "roomJoin"
