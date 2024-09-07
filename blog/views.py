from django.shortcuts import render
from blog.models import Posts


# the index page
def index(request):
    context = {
        "post": Posts.objects.all()
    }
    return render(request, 'assets/index.html', context)

