from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

from .forms import PublicationEditForm, PublicationAddForm
from accounts.models import Publication, Comment


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


def get_publications_list(request):
    publication = Publication.objects.all()
    comment = Comment.objects.all()

    return render(
        request,
        'publications.html',
        context={
            'publication': publication,
            'comment': comment
        }
    )


def add_publication(request):
    if request.method == 'POST':
        form = PublicationAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/publications')

    elif request.method == 'GET':
        form = PublicationAddForm()

    return render(
        request,
        template_name='publication_add.html',
        context={
            'form': form
        }
    )