from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    card = models.CharField(max_length=50)
    period = models.CharField(max_length=50)
    cvv = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.comment