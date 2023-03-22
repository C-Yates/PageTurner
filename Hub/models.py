from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

class UserRating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='userrating')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.book.title} ({self.score})"