from django.urls import path

from accounts.views import add_profile, edit_profile
from .views import get_publications_list, add_publication

app_name = 'publications'

urlpatterns = [
    path('', get_publications_list, name='list'),
    path('add/', add_profile, name='add'),
    path('add/<slug>', add_publication, name='add'),
    path('edit/<slug>', edit_profile, name='edit'),
]