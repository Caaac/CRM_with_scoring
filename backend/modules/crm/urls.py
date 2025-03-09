from django.urls import path, re_path
from . import views
from .views import PageInit, Deal

urlpatterns = [
    # Rest Methods
    path('status/', views.statuses),
    
    # Deal
    # path('deal/', Deal.deal),
    re_path(r'^deal/?$', Deal.deal), # With settings of UF
    re_path(r'^detail/deal/?$', Deal.deal_detail), # With settings of UF
    
    # Init page
    re_path(r'^deal/(?P<mode>kanban|list)/?$', PageInit.crmDealInit),
    
    
    # re_path(r'^company/(?P<pk>[0-9]+)$', views.company_detail),
    
    # # LandingRateTable
    # path('landing-rate/', views.landing_rate_list),
    
    # # CrmDealTable
    # path('crm-deal/', views.crm_deal_list),
    # re_path(r'^crm-deal/(?P<pk>[0-9]+)$', views.crm_deal_detail),
    
    # path('settings/stages/', views.stages),
    # path('settings/source/', views.source),

    # path('managers/', views.managers_list),

    # path('test/', views.test),
]