from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_lenght=255)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField()
    author = models.ForeignKey(User, null=True, on_delete = models.CASCADE)
    likes = models.ManyToManyField(User)

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete = models.CASCADE)