from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.
class Motor(models.Model):
    type = models.CharField(max_length=64)
    model = models.TextField()
    color = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    manufacturer = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type