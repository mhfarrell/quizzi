from django.db import models
from .audit import AuditModel

class Question(AuditModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    question_text = models.TextField()
    score = models.DecimalField(max_digits=5, decimal_places=2)
    topic = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title
