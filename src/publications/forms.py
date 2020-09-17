from django.forms import ModelForm

from .models import Publication


class PublicationBaseForm(ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'


class PublicationEditForm(PublicationBaseForm):
    pass
