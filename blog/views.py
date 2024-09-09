from django.shortcuts import get_object_or_404, render
from blog.models import Posts


# the index page
def index(request):
    context = {
        "post": Posts.objects.all()
    }
    return render(request, 'assets/index.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    return render(request, 'assets/post_detail.html', {'post': post})

