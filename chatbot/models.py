# models.py
from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'chats'  # Set the name of the table to 'chats'

    def __str__(self):
        return f"{self.user.username} - {self.role} - {self.timestamp}"
