from django.shortcuts import render, redirect, HttpResponse


def index(request):

    # response = "Hello"
    # return HttpResponse(response)
    return render(request, 'index.html')
