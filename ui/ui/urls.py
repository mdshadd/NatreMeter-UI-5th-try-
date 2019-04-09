"""ui URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from only import views as only_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',auth_views.LoginView.as_view(template_name='only/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='only/logout.html'),name='logout'),
    path('register/',only_views.register,name='register'),
    path('sign/',only_views.sign_create_view,name='sign'),
    path('home/',only_views.home,name='home'),
    path('upload/',only_views.csv_upload,name='csv_upload'),
    path('processing/',only_views.processing,name='processing'),
]
