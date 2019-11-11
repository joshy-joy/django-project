
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from adoptions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', views.home, name = "home"),
    url('^adoptions/(\d+)/', views.pet_details, name = "pet_details"),
]
