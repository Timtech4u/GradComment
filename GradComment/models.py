from django.db import models
from django.utils import timezone


# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=255)
    reg = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Comments(models.Model):
    student_comment = models.ForeignKey(Students, on_delete=models.CASCADE, null= True)
    comment_text = models.CharField(max_length=255)
    created_on = models.TimeField(timezone.now(), default=timezone.now())

    def __str__(self):
        return self.comment_text
