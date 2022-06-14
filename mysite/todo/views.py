from django.shortcuts import render


def index(request):
    return render(request, 'html_files/index.html')
