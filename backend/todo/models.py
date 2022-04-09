from django.db import models


class TodoModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="name")
    created_at = models.DateTimeField(auto_now=True, verbose_name="created_at")
    updated_at = models.DateTimeField(
        auto_now_add=True, verbose_name="created_at")
    is_done = models.BooleanField(default=False, verbose_name="is_done")

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todo"

    def __str__(self):
        return self.name
