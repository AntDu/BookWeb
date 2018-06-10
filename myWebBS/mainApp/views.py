from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from mainApp.forms import searchForm
from mainApp.models import Author, Book



def index(request):
    """
    1. Create forms
    2. create view vich hendle post and get
    3.create url
    4.render via template (html)
    """

    f = searchForm(request.POST or None)
    if request.method == 'POST' and f.is_valid():
        search_val = f.cleaned_data.get('search_field')
        qs = Author.objects.filter(name__contains=search_val)
        res = []
        for b in qs:
           res.append(b.book_set.all())
        print(res)
        return render(request, 'base.html', {'res': res})



    return render(request, 'base.html', {'form': f})

# @csrf_exempt
# def search_by_author(request):
#     if request.method == 'POST':
#         print(request)
#         redirect('mainApp:index')
#     else:
#         return HttpResponse('GET')
#     return True