
from django.forms import ModelForm
from .models import Name


class NameForm(ModelForm):

    class Meta:
        model = Name
        fields = ('name',)
