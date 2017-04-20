from django.shortcuts import render


def about(request):
    return render(request, 'simple_pages/about.html')