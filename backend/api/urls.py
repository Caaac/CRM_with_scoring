from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('company/', views.company_list),
    re_path(r'^company/(?P<pk>[0-9]+)$', views.company_detail),
]