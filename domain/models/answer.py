from django.db import models
from .audit import AuditModel
from .question import Question

class Answer(AuditModel):  # Inherit AuditModel if tracking is needed
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers'
    )
    answer_text = models.TextField()
    description = models.TextField(blank=True)
    explanation = models.TextField(blank=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.answer_text[:50]}{' ✔' if self.is_correct else ''}"
