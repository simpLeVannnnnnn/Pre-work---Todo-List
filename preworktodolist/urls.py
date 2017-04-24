"""preworktodolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from todo import views

urlpatterns = [
    url(r'^$', views.todo_list, name='todo_list'),
    url(r'^admin/', admin.site.urls),
    url(r'^new_todo/$', views.todo_list),
    url(r'^todo_list/$', views.todo_list),
    url(r'^todo_list/new_todo/$', views.add_todo, name='add'),
    url(r'^todo_list/todo_delete/(?P<id>\d+)/$', views.todo_delete, name='delete'),
    url(r'^todo_list/todo_finish/(?P<id>\d+)/$', views.todo_finish, name='finish'),
    url(r'^todo_list/todo_backout/(?P<id>\d+)/$', views.todo_back, name='backout'),
    url(r'^todo_list/update_todo/(?P<id>\d+)/$', views.update_todo, name='update'),
    url(r'^snippets/$', views.snippet_list, name='serializer'),

]
