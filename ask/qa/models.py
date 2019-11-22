from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.ordering(-'added_at')
    def popular(self):
        return self.ordering('rating')

class Question(models.Model):
    title = models.CharField(max_lenght=255)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField()
    author = models.ForeignKey(User, null=True, on_delete = models.CASCADE)
    likes = models.ManyToManyField(User)
    objects = QuestionManager()

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete = models.CASCADE)
