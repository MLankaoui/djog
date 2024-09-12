from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from blog.froms import createUserForm
from blog.models import Posts
from django.db.models import Q

# the index page
def index(request):
    context = {
        "post": Posts.objects.all()
    }
    return render(request, 'assets/index.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    return render(request, 'assets/post_detail.html', {'post': post})


def search_view(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Posts.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    context = {
        'results': results,
        'query': query,
    }

    return render(request, 'assets/search_results.html', context)


def register_page(request):
    form = createUserForm()
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            # getting username
            user_name = form.cleaned_data.get('username')
            messages.success(request, f'account created with the username : {user_name}')
            return redirect('home')  # Redirect to the login page or another page after successful registration
    context = {"form": form}
    return render(request, 'assets/signup.html', context)