from turtle import title
from django.contrib.auth.models import User
from django.db import models
DEFAULT_STATUS = "draft"
STATUS = [
    # left side: DB
    # right side: human-readable name
    ('draft', 'Qaralama'),
    ('published', 'Nəşr edildi'),
    ('deleted', 'Silindi'),
]

class Carusel(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    cover_image = models.ImageField(
        upload_to='carousel',
        null=True,
        blank=True,
    )
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=15
    )
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(
        upload_to='service',
        null=True,
        blank=True,
    )
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=15
    )
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    def __str__(self):
        return self.title

class Project(models.Model):
    project_name = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=400, blank=True, null=True)
    image = models.ImageField(
        upload_to='project',
        null=True,
        blank=True,
    )
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=15
    )
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    def __str__(self):
        return self.project_name




class Category(models.Model):
    title=models.CharField(max_length=200)

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.title



class Blog(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content  = models.TextField() 
    image = models.ImageField(
        upload_to='blog',
        null=True,
        blank=True,
    )
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=15
    )
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   

    class Meta:
        verbose_name_plural='Blog'

    def __str__(self):
        return self.title

class Comment(models.Model):
    news=models.ForeignKey(Blog,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    comment=models.TextField()
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=15
    )
    class Meta:
        verbose_name_plural='Comments'

    