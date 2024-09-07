from django.urls import path
from blog.views import index
from djogo import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
