# coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.template import RequestContext
from .models import Todo
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from todo.serializers import TodoSerializer
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def todo_list(request):
    todo_list = Todo.objects.filter(todo_sign=1)
    finish_todo = Todo.objects.filter(todo_sign=0)
    # paginator = Paginator(todo_list, 3)
    # fpaginator = Paginator(finish_todo, 3)
    # page = request.GET.get('page')
    # fpage = request.GET.get('fpage')
    # try:
    #      todo_list = paginator.page(page)
    # except PageNotAnInteger:
    #      todo_list = paginator.page(1)
    #  except EmptyPage:
    # todo_list = paginator.page(paginator.num_pages)
    # try:
    #     finish_todo = fpaginator.page(fpage)
    # except PageNotAnInteger:
    #     finish_todo = fpaginator.page(1)
    # except EmptyPage:
    #    finish_todo = fpaginator.page(fpaginator.num_pages)
    return render_to_response('todo_list.html', {'todo_list': todo_list, 'finish_todo': finish_todo},
                              context_instance=RequestContext(request))

def add_todo(request):
    if request.method == 'POST':
        if request.method == 'POST':
            atodo = request.POST['todo']
            todo_priority = request.POST['todo_priority']
            # expire_date = request.POST['expire_date']
            todo = Todo(todo=atodo, todo_priority=todo_priority, todo_sign='1')   # expire_date=expire_date
            try:
                todo.save()
            except Exception:
                raise Http404

        todo_list = Todo.objects.filter(todo_sign=1)
        finish_todo = Todo.objects.filter(todo_sign=0)
        # paginator = Paginator(todo_list, 3)
        # fpaginator = Paginator(finish_todo, 3)
        # page = request.GET.get('page')
        # fpage = request.GET.get('fpage')
        # try:
        #     todo_list = paginator.page(page)
        # except PageNotAnInteger:
        #    todo_list = paginator.page(1)
        # except EmptyPage:
        #     todo_list = paginator.page(paginator.num_pages)
        # try:
        #     finish_todo = fpaginator.page(fpage)
        # except PageNotAnInteger:
        #     finish_todo = fpaginator.page(1)
        # except EmptyPage:
        #     finish_todo = fpaginator.page(fpaginator.num_pages)
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
        # expire_date = request.POST['expire_date']
        todo = Todo.objects.get(id=id)
        # todo.expire_date = expire_date
        todo.todo = atodo
        todo.todo_priority = todo_priority
        todo.todo_sign = '1'
        try:
            todo.save()
        except Exception:
            raise Http404
        todo_list = Todo.objects.filter(todo_sign='1')
        finish_todo = Todo.objects.filter(todo_sign=0)
        #  = Paginator(todo_list, 3)
        # fpaginator = Paginator(finish_todo, 3)
        # page = request.GET.get('page')
        # fpage = request.GET.get('fpage')
        # try:
        #     todo_list = paginator.page(page)
        # except PageNotAnInteger:
        #     todo_list = paginator.page(1)
        # except EmptyPage:
        #     todo_list = paginator.page(paginator.num_pages)
        # try:
        #   finish_todo = fpaginator.page(fpage)
        # except PageNotAnInteger:
        #     finish_todo = fpaginator.page(1)
        # except EmptyPage:
        #    finish_todo = fpaginator.page(fpaginator.num_pages)
        return render_to_response('todo_list.html', {'todo_list': todo_list, 'finish_todo': finish_todo},
                                  context_instance=RequestContext(request))
    else:
        todo = Todo.objects.get(id=id)
        return render_to_response('updata.html', {'todo': todo}, context_instance=RequestContext(request))


# def listing(request):
#    contact_list = Todo.objects.all()
#    paginator = Paginator(contact_list, 25) # Show 25 contacts per page
#    page = request.GET.get('page')
#   try:
#       contacts = paginator.page(page)
#    except PageNotAnInteger:
#       contacts = paginator.page(1)
#    except EmptyPage:
#        contacts = paginator.page(paginator.num_pages)
#    return render_to_response('todo_list.html', {"contacts": contacts})


@csrf_exempt
def snippet_list(request):

    if request.method == 'GET':
        todo = Todo.objects.all()
        serializer = TodoSerializer(todo, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)