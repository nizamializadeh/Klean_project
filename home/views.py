from django.shortcuts import get_object_or_404, render

from home.models import Blog, Carusel, Category, Project, Service,Comment
from django.db.models import Q,Count
from django.contrib import messages
STATUS = "published"

# Create your views here.
def carusel(request):
    carusels=Carusel.objects.filter(status=STATUS)
    services=Service.objects.filter(status=STATUS)
    projects=Project.objects.filter(status=STATUS)
    blogs=Blog.objects.filter(status=STATUS)
    return render(request,"index.html",{'carusels':carusels,'services':services,'projects':projects,'blogs':blogs})

def about(request):
    return render(request,"about.html")
def service(request):
    return render(request,"service.html")
def contact(request):
    return render(request,"contact.html")
def project(request):
    return render(request,"project.html")

    
def detail(request,slug):
    context = dict()
    context['blog'] = get_object_or_404(Blog, slug=slug)
    context['categories'] = Category.objects.all().annotate(blogs_count=Count('blog', filter=Q(blog__status=STATUS)))[0:5]
    context['posts'] = Blog.objects.filter(status=STATUS).order_by('-createt_at')[0:5]
    context['comments']=Comment.objects.filter(news = context['blog'],status=STATUS).order_by('-id')

    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        comment=request.POST['comment']
        Comment.objects.create(
            news=context['blog'],
            name=name,
            email=email,
            comment=comment
        )
        
        messages.success(request,'Comment submitted but in moderation mode.')

    return render(request, 'blog_detail.html', context)

