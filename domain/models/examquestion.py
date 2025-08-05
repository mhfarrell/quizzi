from django.db import models
from .exam import Exam
from .question import Question

class ExamQuestion(models.Model):
    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name='exam_questions'
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='exam_instances'
    )

    class Meta:
        unique_together = ('exam', 'question')

    def __str__(self):
        return f"{self.exam.title} → {self.question.title}"
