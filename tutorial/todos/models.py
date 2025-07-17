from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=64)
    kind = models.CharField(max_length=16, null=True)  
    description = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)

class Teacher(models.Model):
    name = models.CharField(max_length=64)
    class_name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=64)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.title

