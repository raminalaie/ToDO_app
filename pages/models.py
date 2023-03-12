from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime


class Post(models.Model):
    status_list = (
        ("yes", "Done"),
        ("no", "NotDOne")
    )
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    status = models.CharField(max_length=250, choices=status_list, default="Done")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
