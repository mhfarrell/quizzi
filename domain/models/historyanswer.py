from django.db import models
from .history import History
from .answer import Answer

class HistoryAnswer(models.Model):
    history = models.ForeignKey(
        History,
        on_delete=models.CASCADE,
        related_name='selected_answers'
    )
    answer = models.ForeignKey(
        Answer,
        on_delete=models.CASCADE,
        related_name='history_entries'
    )

    def __str__(self):
        return f"Answer {self.answer_id} for History {self.history_id}"
