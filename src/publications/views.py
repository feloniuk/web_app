from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

from accounts.forms import PublicationEditForm
from accounts.models import Publication


def edit_publication(request, slug):
    try:
        profile = Publication.objects.get(id=slug)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Profile id {slug} doesnt exist')
    if request.method == 'POST':
        form = PublicationEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/profiles/show/{slug}')

    elif request.method == 'GET':
        form = PublicationEditForm(instance=profile)

    return render(
        request,
        template_name='profile_edit.html',
        context={
            'form': form
        }
    )
