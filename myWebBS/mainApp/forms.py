from django import forms
from django.forms import SelectDateWidget

from mainApp.models import Author


# Формы не выводятся на страницу
# Не большие вопросы по шаблонам Django и их расширению

class SearchForm(forms.Form):
    search_field = forms.CharField()


# class AddAuthorForm(forms.Form):
#     name = forms.CharField(max_length=32)
#     surname = forms.CharField(max_length=64)
#     age = forms.IntegerField(max_value=130)


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'age']




#




