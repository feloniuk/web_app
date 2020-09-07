from django.db import models


# Create your models here.
class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=64)
    nickname = models.CharField(max_length=124, unique=True, default=login)

    def __str__(self):
        return f'{self.nickname}'


class Publication(models.Model):
    author = models.ManyToManyField(Profile, related_name='author_p')
    description = models.CharField(max_length=255)
    release_date = models.DateTimeField(auto_now_add=True)
    publication = models.FileField(upload_to='media/')

    def __str__(self):
        return '.join(author.login for author in self.author.all())'


class Comment(models.Model):
    author = models.ForeignKey(Profile, related_name='author_c', verbose_name='author',
                               on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, related_name='publication_c', verbose_name='publication',
                                    on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    release_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'author - {self.author}'
