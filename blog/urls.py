from django.urls import path,include
from . import views

app_name='blog'

from django.conf.urls.static import static  #added to add static for photos

from django.conf import settings #added to add settings.py reflection

urlpatterns = [

    path('', views.all_blogs,name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),



]
