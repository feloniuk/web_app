from django.db import models


class Publication(models.Model):
    author = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE,
                               related_name='author_p')
    description = models.CharField(max_length=255)
    release_date = models.DateTimeField(auto_now_add=True)
    publication = models.FileField(upload_to='media/')

    def __str__(self):
        return f'author - {self.author}:{self.description}'
