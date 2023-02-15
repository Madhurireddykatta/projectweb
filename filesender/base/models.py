from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Transfer(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='file_sender')
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name='file_reciever')
    file = models.FileField(upload_to='uploads/')
    filename = models.CharField(max_length=200)

    def __str__(self):
        return self.filename