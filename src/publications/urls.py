from django.urls import path

from .views import get_publications_list, add_publication, edit_publication

app_name = 'publications'

urlpatterns = [
    path('', get_publications_list, name='list'),
    path('add', add_publication, name='add'),
    path('edit/<slug>', edit_publication, name='edit'),
]
