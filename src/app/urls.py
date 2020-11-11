"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from app import settings

app_name = 'app'

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('profiles/', include('accounts.urls')),
                  path('', include('accounts.urls')),
                  path('publications/', include('publications.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#[
#    path('admin/', admin.site.urls),
#    path('publications/', views.get_publications_list),
#    path('profiles/', views.ProfilesListView.as_view()),
#    path('profiles/add/', views.ProfileCreateView.as_view()),
#    path('profiles/show/<slug>', views.get_profile),
#    path('profiles/edit/<slug>', views.edit_profile),
#    path('', views.get_publications_list, name='home')
#]
