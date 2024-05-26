from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    # CompanyTable
    path('company/', views.company_list),
    re_path(r'^company/(?P<pk>[0-9]+)$', views.company_detail),
    
    # LandingRateTable
    path('landing-rate/', views.landing_rate_list),
    
    # CrmDealTable
    path('crm-deal/', views.crm_deal_list),
    re_path(r'^crm-deal/(?P<pk>[0-9]+)$', views.crm_deal_detail),
    
    path('settings/stages/', views.stages),
    path('settings/source/', views.source),

    path('managers/', views.managers_list),

    path('test/', views.test),
]