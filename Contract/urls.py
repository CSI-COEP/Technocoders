"""Contract URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from main.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('contractor_login', contractor_login, name="contractor_login"),
    path('government_login', government_login, name="government_login"),
    path('contractor_signup', contractor_signup, name="contractor_signup"),
    path('government_signup', government_signup, name="government_signup"),
    path('contractor_home', contractor_home, name="contractor_home"),
    path('government_home', government_home, name="government_home"),
    path('Logout', Logout, name="Logout"),
    path('contractor_changepassword', contractor_changepassword,
         name="contractor_changepassword"),
    path('government_changepassword', government_changepassword,
         name="government_changepassword"),
    path('add_contract', add_contract, name="add_contract"),
    path('contracts_list', contracts_list, name="contracts_list"),
    #path('edit_jobdetail/<int:pid>', edit_jobdetail, name="edit_jobdetail"),
    path('contractor_contractslist', contractor_contractslist,
         name="contractor_contractslist"),
    #path('user_apply', user_apply, name="user_apply"),
    path('contractors_applied', contractors_applied, name="contractors_applied"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
