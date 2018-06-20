from django import forms
from django.forms import SelectDateWidget

from mainApp.models import Author


# Формы не выводятся на страницу
# Не большие вопросы по шаблонам Django и их расширению

class SearchForm(forms.Form):
    search_field = forms.CharField()

"""
Ты доку открывал?
# Create the form class.
>>> class ArticleForm(ModelForm):
...     class Meta:
...         model = Article
...         fields = ['pub_date', 'headline', 'content', 'reporter']
https://docs.djangoproject.com/en/1.11/topics/forms/modelforms/
"""
class AddAuthorForm(forms.Form):
    name = forms.CharField(max_length=32)
    surname = forms.CharField(max_length=64)
    age = forms.IntegerField(max_value=130)


# Так создавали форму на занятиях но у меня не выходит создать таким способом

# from django import forms
# from django.forms import SelectDateWidget
# from ipdb import set_trace
#
# from blog.models import Post
#
#
# class CreatePostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('title', 'text', 'published_date')
#
#     def __init__(self, user, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.user = user
#         self.fields['published_date'].widget = SelectDateWidget()
#
#
#     def save(self, commit=True):
#         post = self.instance
#         post.author = self.user
#         super().save()




