# coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from .models import Todo


def todo_list(request):
    todo_list = Todo.objects.filter(todo_sign=1)
    finish_todo = Todo.objects.filter(todo_sign=0)
    return render_to_response('todo_list.html', {'todo_list': todo_list, 'finish_todo': finish_todo},
                              context_instance=RequestContext(request))

def add_todo(request):
    if request.method == 'POST':
        atodo = request.POST['todo']
        todo_priority = request.POST['todo_priority']
        todo = Todo(todo=atodo, todo_priority=todo_priority, todo_sign='1')
        todo.save()
        todo_list = Todo.objects.filter(todo_sign=1)
        finish_todo = Todo.objects.filter(todo_sign=0)
        return render_to_response('todo_list.html', {'todo_list': todo_list, 'finish_todo': finish_todo},
                                  context_instance=RequestContext(request))
    else:
        return render_to_response('new_todo.html', context_instance=RequestContext(request))


def todo_delete(request, id=''):
    todo = Todo.objects.get(id=id)
    if todo:
        todo.delete()
        return HttpResponseRedirect('/todo_list/')
    todo_list = Todo.objects.filter(todo_sign=1)
    finish_todo = Todo.objects.filter(todo_sign=0)
    return render_to_response('todo_list.html', {'todo_list': todo_list, 'finish_todo': finish_todo},
                              context_instance=RequestContext(request))

def todo_finish(request, id=''):
    todo = Todo.objects.get(id=id)
    if todo.todo_sign == '1':
        todo.todo_sign = '0'
        todo.save()
        return HttpResponseRedirect('/todo_list/')
    todo_list = Todo.objects.filter(todo_sign=1)
    finish_todo = Todo.objects.filter(todo_sign=0)
    return render_to_response('todo_list.html', {'todo_list': todo_list, 'finish_todo': finish_todo},
                              context_instance=RequestContext(request))

def todo_back(request, id=''):
    todo = Todo.objects.get(id=id)
    if todo.todo_sign == '0':
        todo.todo_sign = '1'
        todo.save()
        return HttpResponseRedirect('/todo_list/')
    todo_list = Todo.objects.filter(todo_sign=1)
    finish_todo = Todo.objects.filter(todo_sign=0)
    return render_to_response('todo_list.html', {'todo_list': todo_list, 'finish_todo': finish_todo},
                              context_instance=RequestContext(request))


def update_todo(request, id=''):

    if request.method == 'POST':
        atodo = request.POST['todo']
        todo_priority = request.POST['todo_priority']
        todo = Todo.objects.get(id=id)
        todo.todo = atodo
        todo.todo_priority = todo_priority
        todo.todo_sign = '1'
        todo.save()
        todo_list = Todo.objects.filter(todo_sign='1')
        finish_todo = Todo.objects.filter(todo_sign=0)
        return render_to_response('todo_list.html', {'todo_list': todo_list, 'finish_todo': finish_todo},
                                  context_instance=RequestContext(request))
    else:
        todo = Todo.objects.get(id=id)
        return render_to_response('updata.html', {'todo': todo}, context_instance=RequestContext(request))
