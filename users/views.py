from django.template import RequestContext
from django.shortcuts import render_to_response,render

# Create your views here.
from django.http import HttpResponse

from .models import Users

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