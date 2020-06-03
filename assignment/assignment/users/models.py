from django.db import models
import uuid

# Create your models here.

class User(models.Model):
    id                   = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    real_name            = models.CharField(max_length=64)
    tz                   = models.CharField(max_length=64)
    class Meta:
        ordering = ['real_name']


class ActivityPeriod(models.Model):
    id                   = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    start_time           = models.DateTimeField(auto_now_add=True, blank=True)
    end_time             = models.DateTimeField(auto_now_add=True, blank=True)
    user                 = models.ForeignKey(User, related_name='activity_period', on_delete=models.CASCADE, blank=True,null=True)
    class Meta:
        ordering = ['id']