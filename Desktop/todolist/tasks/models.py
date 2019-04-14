from django.db import models
from django.urls import reverse,reverse_lazy
# Create your models here.
class Tasks(models.Model):
    TaskName = models.CharField(max_length = 100)
    Description = models.CharField(max_length = 400)
    DueDate = models.DateField()
    priority = models.IntegerField()

    def __str__(self):
        return self.TaskName
    def get_absolute_url(self):
        return reverse('tasks:detail',kwargs={'pk':self.pk})
