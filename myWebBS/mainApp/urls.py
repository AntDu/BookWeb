from django.conf.urls import url

from . import views

app_name = 'mainApp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_author/$', views.add_author, name='add-author'),
]