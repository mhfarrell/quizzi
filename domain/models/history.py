from django.db import models
from django.contrib.auth import get_user_model
from .exam import Exam

User = get_user_model()

class History(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='exam_histories'
    )
    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name='exam_histories'
    )
    score = models.DecimalField(max_digits=5, decimal_places=2)
    taken_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.exam.title} ({self.score})"
