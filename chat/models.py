from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class Thread(models.Model):
    participants = models.ManyToManyField(get_user_model())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.participants.count() > 2:
            raise ValidationError('A Thread cannot have more than 2 participants.')


class Message(models.Model):
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
