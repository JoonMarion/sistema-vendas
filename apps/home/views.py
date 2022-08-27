from django.shortcuts import render


# HOMEPAGE
def home(request):
    return render(request, 'index.html')