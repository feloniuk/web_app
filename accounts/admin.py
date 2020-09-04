from django.contrib import admin
from .models import Profile, Comment, Publication

# Register your models here.
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Publication)

