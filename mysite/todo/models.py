from django.db import models


class Todo(models.Model):
    objects = models.Manager()
    task = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.task
