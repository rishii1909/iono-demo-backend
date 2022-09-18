from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import json
# Create your models here.

class BatchRunModel(models.Model):

    class Meta:
        verbose_name = "Batch Run"

    queries = models.TextField()
    results = models.TextField(null=True)
    created_at = models.DateTimeField( auto_now=False, auto_now_add=True)
    done = models.BooleanField(default=False)
    owner = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)

    def __str__(self):

        return f"{self.owner.first_name}'s log"