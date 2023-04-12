from django.contrib.auth import get_user_model
from django.db import models


class Thread(models.Model):
    participants = models.ManyToManyField(get_user_model())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Thread'
        verbose_name_plural = 'Threads'

    def __str__(self):
        return f"Thread id: {self.id}"


class Message(models.Model):
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return f'Message id: {self.id}'
