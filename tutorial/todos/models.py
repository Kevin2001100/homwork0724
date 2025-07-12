from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=64)
    kind = models.CharField(max_length=16, null=True)  
    description = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

