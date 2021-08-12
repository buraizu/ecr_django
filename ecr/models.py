from django.db import models
from django.contrib.auth.models import User

class Run(models.Model):
    course = models.CharField(max_length=100)
    review = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    rating = models.IntegerField(null=True)
    distance = models.IntegerField()
    time = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.course

