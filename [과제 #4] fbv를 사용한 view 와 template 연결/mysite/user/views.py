from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def get_user(request: HttpRequest):
    context = {
        'posts': [
            {
                'content':
            }
        ]
    }
    return render(request, 'dojo/sample.html', context)
