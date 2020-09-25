from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# your created models here.
from publications.models import Publication


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nickname = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.user}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, nickname=instance.email)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Comment(models.Model):
    author = models.ForeignKey(Profile, related_name='author_c', verbose_name='author',
                               on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, related_name='publication_c', verbose_name='publication',
                                    on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    release_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'author - {self.author}'


class Following(models.Model):
    profile_id = models.ForeignKey(Profile, related_name="following", on_delete=models.CASCADE)
    following_profile_id = models.ForeignKey(Profile, related_name="followers", on_delete=models.CASCADE)

    # You can even add info about when user started following
    created = models.DateTimeField(auto_now_add=True)
