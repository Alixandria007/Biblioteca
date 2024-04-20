from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from . import models

class LeitorForm(ModelForm):

    data_nascimento = forms.DateField(
        label = "Nascimento",
        widget=forms.DateInput(attrs={ "type":"date"})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = models.Leitor
        fields = ('__all__')
        exclude = "leitor",

class UserForm(ModelForm):
    
    first_name = forms.CharField(
        label = "Nome",
        required = True
    )

    last_name = forms.CharField(
        label = "Sobrenome",
        required = True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.help_text = ""

    class Meta:

        model = User
        fields = "first_name", "last_name", "email"

    def clean(self, *args, **kwargs):
        cleaned_data = self.cleaned_data

        email_data = cleaned_data['email']

        if User.objects.filter(email = email_data).exists():
            self.add_error(
                'email',
                ValidationError('Esse Email já existe.')
            )

        return super().clean()