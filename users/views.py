from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.
from django.http import HttpResponse

from .models import Users

def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    users_list = Users.objects.order_by('user_id')[:10]
    output = {'users_list': users_list}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('users/index.html', output, context)