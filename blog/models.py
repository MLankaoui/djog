from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Posts(models.Model):
    title = models.CharField(max_length=50, null=False)
    author = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    content = RichTextField(null=True, blank=True)
    # content = models.TextField(max_length=400, default='')
    created_at = models.DateField(auto_now=False, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='uploads', default='')

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = 'Posts'
        ordering = ['-created_at'] # newest post first
