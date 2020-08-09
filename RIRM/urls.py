"""RIRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from onlineform import views
from onlineform.views import ClientListView,ClientDetailView,ClientUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.onlineform,name='onlineform'),
    path('getdetail',views.getdetail,name='getdetail'),
    path('filteredlist',views.filteredlist,name='filteredlist'),

    path('clientlist/', ClientListView.as_view(),name='client-list'),
    path('client/<int:pk>/', ClientDetailView.as_view(),name='client-detail'),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(),name='client-update'),
    


]
