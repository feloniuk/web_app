from django.db import models


# Create your models here.
class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=64)
    nickname = models.CharField(max_length=124, unique=True, default=login)

    def __str__(self):
        return f'nickname - {self.nickname}, id - {self.id}, password - {self.password}'


class Publication(models.Model):
    author = models.ManyToManyField(Profile)
    description = models.CharField(max_length=255)
    release_date = models.DateTimeField(auto_now_add=True)
    publication = models.FileField(upload_to='media/')

    def __str__(self):
        return f'author - {self.author}'


class Comment(models.Model):
    author = models.ManyToManyField(Profile)
    comment = models.CharField(max_length=255)
    release_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'author - {self.author}'
