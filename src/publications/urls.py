from django.urls import path
from .views import get_publications_list
from accounts.views import get_profile, add_profile, edit_profile

app_name = 'publications'

urlpatterns = [
    path('', get_publications_list, name='list'),
    path('add/', add_profile, name='add'),
    path('show/<id>', get_profile, name='show'),
    path('edit/<id>', edit_profile, name='edit'),
]