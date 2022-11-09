from django.shortcuts import render

def company(request):
    return render(request, 'index.html')

def samsung(request):
    return render(request, 'samsung.html')

def apple(request):
    return render(request, 'apple.html')

def artel(request):
    return render(request, 'artel.html')

