from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('classes/', views.classes, name='classes'),
    path('pricing/', views.pricing, name='pricing'),
    path('news/', views.news, name='news'),
    path('contact/', views.contact, name='contact'),
]