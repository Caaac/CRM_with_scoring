from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path(r'^company$', views.company_list),
    path('company/', views.company_list),
    # path(r'^company/(?P<pk>[0-9]+)$', views.company_detail),
    # path(r'^company/$', views.company),
]