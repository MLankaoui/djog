from django.shortcuts import render


# the index page
def index(request):
    return render(request, 'assets/index.html')