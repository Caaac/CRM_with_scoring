"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from backend.settings import DEBUG, MEDIA_URL, MEDIA_ROOT

from . import views, auth

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/', include('api.urls')),
    path('api/v1/crm/', include('modules.crm.urls')),
    
    re_path(r'^(?P<mode>install|uninstall)/(?P<module>[a-z]+)/?$', views.db_control),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('auth/login/', auth.Auth.login),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)