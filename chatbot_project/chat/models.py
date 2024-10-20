from django.db import models

# Create your models here.

class Conversation(models.Model):
    user_message = models.TextField(blank=True, null=True)
    bot_response = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class UploadedFile(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="files")
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"File: {self.file.name}"
