from django.contrib import admin
from .models import Profile, Comment, Publication, Following

# Register your models here.
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Publication)
admin.site.register(Following)

