from django.shortcuts import render
from blog.models import Posts
import random


# the index page
def index(request):
    context = {
        "post": Posts.objects.all()
    }
    return render(request, 'assets/index.html', context)


def side_bar(request):
    post_ids = Posts.objects.values_list('id', flat=True)
    random_id = random.choice(post_ids)
    context = {
        "random_post": Posts.objects.get(pk=random_id)
    }
    return render(request, 'assets/side.html', context)