from django.urls import path, re_path
from . import views

urlpatterns = [
    # Rest Methods
    path('status/', views.statuses),
    
    # Deal
    re_path(r'^deal/?$', views.Deal.deal), # With settings of UF # Not used bit not deprecated
    re_path(r'^detail/deal/?$', views.DealDetail.as_view()), # With settings of UF
    
    # Init page
    re_path(r'^deal/(?P<mode>kanban|list)/?$', views.PageInit.crmDealInit),

    # Settings
    ## User-Field
    re_path(r'^settings/user-field/?$', views.UserFieldsListView.as_view()),
    re_path(r'^settings/user-field-detail/?$', views.UserFieldDetailsView.as_view()),
]