from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from accounts.forms import ProfileAddForm, ProfileEditForm
from accounts.models import Profile
from app import settings


class ProfilesListView(ListView):
    model = Profile
    template_name = 'profiles.html'
    context_object_name = 'result'

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            qs = qs.filter(Q(nickname__icontains=search) | Q(login__icontains=search))
        return qs


class ProfileCreateView(PermissionRequiredMixin, CreateView):
    model = Profile
    template_name = 'profile_add.html'
    form_class = ProfileAddForm
    permission_required = ('accounts.add_profile',)

    def get_success_url(self):
        return reverse('home')


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'
    pk_url_kwarg = 'item_id'


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'profile_add.html'
    form_class = ProfileEditForm
    pk_url_kwarg = 'item_id'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        print(kwargs['instance'].user.username)
        if self.request.user != kwargs['instance'].user \
                and \
                not (self.request.user.groups.filter(name=settings.ADMIN_GROUP).exists()):
            return self.handle_no_permission()

        return kwargs

    def get_success_url(self):
        return reverse('profiles:list')


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'profile_add.html'
    success_url = '/profiles/'
    success_msg = 'Successful deleted'
    pk_url_kwarg = 'item_id'

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)

    def delete(self, request, *args, **kwargs):
        self.object = User.get_object()
        if self.request.user != self.object \
                and not (self.request.user.groups.filter(name='admin_application').exists()):
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
