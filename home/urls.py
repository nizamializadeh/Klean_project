
from django.urls import path,include,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.carusel, name='index'),
    path("about", views.about, name='about'),
    path("service", views.service, name='service'),
    path("project", views.project, name='project'),
    path("contact", views.contact, name='contact'),
    path('news/<slug:slug>/', views.detail, name='detail'),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)