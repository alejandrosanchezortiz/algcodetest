from django.template import RequestContext
from django.shortcuts import render_to_response,render
from django.views.generic import ListView
from django.db import connection

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect

from .models import Users
from .forms import UsersForm

def add_connection(request):
    id1=request.GET.get('id1')
    id2=request.GET.get('id2')
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO users_users_connects (from_users_id,to_users_id) values(%s,%s)", (id1,id2))
        cursor.execute("INSERT INTO users_users_connects (from_users_id,to_users_id) values(%s,%s)", (id2,id1))
    context = RequestContext(request)
    users_list = Users.objects.order_by('user_id')
    output = {'users_list': users_list}
    return render_to_response('users/connect_users.html', output, context)

def delete_user(request):
    id=request.GET.get('user_id')
    object = Users.objects.get(user_id=id)
    object.delete()
    
    context = RequestContext(request)
    users_list = Users.objects.order_by('user_id')
    output = {'users_list': users_list}
    return render_to_response('users/view_connections.html', output, context)

def connect_users(request):
    context = RequestContext(request)

    users_list = Users.objects.order_by('user_id')
    output = {'users_list': users_list}
    
    return render_to_response('users/connect_users.html', output, context)

def view_connections(request):
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    users_list = Users.objects.order_by('user_id')
    output = {'users_list': users_list}
    
    return render_to_response('users/view_connections.html', output, context)
    
def add_user(request):
    submitted = False
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_user/?submitted=True')
    else:
        form = UsersForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'users/add_user.html', {'form': form, 'submitted': submitted})

def view_chart(request):
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    users_list = Users.objects.order_by('user_id')[:10]
    output = {'users_list': users_list}

    return render_to_response('users/view_chart.html', output, context)

def index(request):
    title = " Users Connections - Code Test -"
    return render(request, 'users/home.html', {'title': title})