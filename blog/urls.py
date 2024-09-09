from django.urls import path
from blog.views import index, post_detail, search_view
from djogo import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='home'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('search/', search_view, name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
