from user.models import User
from django.db import models


from mentor.base_model import BaseModel
from mentor.room import Room

class Message(BaseModel):
    message = models.CharField(max_length=500)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message", db_column="user_id")
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="message", db_column="room_id")

    class Meta:
        db_table = "message"

    def __str__(self):
        return self.user_id.user_id

    def last_30_messages(self, room_id):
        return Message.objects.filter(room_id=room_id).order_by('created_at')[:50]