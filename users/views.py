from django.template import RequestContext
from django.shortcuts import render_to_response,render
from django.views.generic import ListView

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect

from .models import Users
from .forms import UsersForm

def delete_user(request,user_id =None):
    object = Users.objects.get(id=user_id)
    object.delete()
    return render(request,'users/home.html')

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