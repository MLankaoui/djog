from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=50, null=False)
    author = models.CharField(max_length=50, null=False)
    content = models.TextField(max_length=400, default='')
    created_at = models.DateField(auto_now=False, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='uploads', default='')

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = 'Posts'
        ordering = ['-created_at'] # newest post first
