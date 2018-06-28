from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class Grade(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="班级名字"
    )
    type = models.CharField(
        max_length=20,
        verbose_name="班级类型"
    )
    def __str__(self):
        return self.name



class Stu(models.Model):
    name = models.CharField(
        max_length = 20,
        verbose_name = "名字"
    )
    age = models.IntegerField(
        default=18,
        verbose_name="年纪"
    )
    score = models.IntegerField(
        verbose_name="成绩"
    )
    grade = models.ForeignKey(
        Grade,
        verbose_name="所属班级",
        null = True
    )
    def __str__(self):
        return self.name






class MyBook(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="书名"
    )
    content = HTMLField()

