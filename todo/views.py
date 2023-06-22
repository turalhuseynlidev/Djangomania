from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from django.http import Http404
from .models import Todo, Category, Tag


#HOMEPAGE
@login_required(login_url='/admin/login/')
def home_view(request):
    todos = Todo.objects.filter(
         user=request.user,
         is_active=True
         )
    context = dict(
        todos = todos
    )
    return render(request, 'todo/todo_list.html', context)


#Category_page
@login_required(login_url='/admin/login/')
def category_view(request, category_slug):
    category = get_object_or_404(Category, slug = category_slug)
    todos = Todo.objects.filter(
         user=request.user,
         is_active=True,
         category=category
    )
    context = dict(
        category=category,
        todos = todos,
    )
    return render(request, 'todo/todo_list.html', context)



#DETAIL PAGE
@login_required(login_url='/admin/login/')
def todo_detail_view(request, category_slug, id):
        todo = get_object_or_404(Todo, category__slug=category_slug,  pk=id, user=request.user)
        context = dict(
            todo = todo,
            todos = Todo.objects.filter(is_active=True)
    )
        return render(request, 'todo/todo_detail.html', context)

@login_required(login_url='/admin/login/')
def tag_view(request, tag_slug):
     tag = get_object_or_404(Tag, slug=tag_slug)
     context = dict(
          tag = tag,
          todos = tag.todo_set.filter(user=request.user),
     )
     return render(request, 'todo/todo_list.html', context)