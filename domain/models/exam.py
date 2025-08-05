from django.db import models
from django.utils.timezone import now
from .audit import AuditModel

class Exam(AuditModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    topic = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    created_date = models.DateField(default=now)

    class Meta:
        unique_together = ('title', 'created_by', 'created_date')
