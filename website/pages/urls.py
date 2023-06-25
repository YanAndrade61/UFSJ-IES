from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('galery/', views.galery, name='galery'),
    path('workshop/', views.workshop, name='workshop'),
    path('login/', views.login, name='login'),
]