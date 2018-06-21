from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from mainApp.forms import SearchForm, AddAuthorForm
from mainApp.models import Author, Book


def index(request):
    """
    1. Create forms
    2. create view vich hendle post and get
    3.create url
    4.render via template (html)
    """
    f = SearchForm(request.POST or None)
    if request.method == 'POST' and f.is_valid():
        search_val = f.cleaned_data.get('search_field')
        qs = Author.objects.filter(Q(name__icontains=search_val) | Q(surname__icontains=search_val))
        res = [b.book_set.all() for b in qs]
        # res = []
        # for b in qs:
        #    res.append(b.book_set.all())
        print(res)
        return render(request, 'search_book.html', {'res': res, 'form': f})
    return render(request, 'search_book.html', {'form': f})

# Глобальный контекст или же контекстт  процессов
#


def add_author(request):


    form = AddAuthorForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect(reverse('main:index'))

    return render(request, 'add_author.html', {'add_author_form': form})


