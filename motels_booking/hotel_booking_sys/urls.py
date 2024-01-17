"""hotel_booking_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.user_login, name='login'),  # login
    path('logout/', views.user_logout, name='logout'),  # logout
    path('user_info/', views.user_info, name='user_info'),  # User modifies basic information
    path('change_pwd/', views.change_pwd, name='change_pwd'),  # User modifies password

    path('register/', views.register, name='register'),  # registration(admin control)
    path('user_register/', views.user_register, name='user_register'),  # Registered user (administrator operation)
    path('user_list/', views.user_list, name='user_list'),  # Administrator interface user list
    path('update_pwd/<int:id>', views.update_pwd, name='update_pwd'),  # Administrator updates password
    path('user_active/<int:id>', views.user_active, name='user_active'),  # Administrator modifies user status

    path('', views.index, name='index'),  # search page
    path('hotel_list/', views.hotel_list, name='hotel_list'),  # Search hotel list page
    path('hotel_manage_list/', views.hotel_manage_list, name='hotel_manage_list'),  # Hotel Management List
    path('hotel_manage_detail/', views.hotel_manage_detail, name='hotel_manage_add'),  # Hotel Management View: Add
    path('hotel_manage_detail/', views.hotel_manage_detail, name='hotel_manage_add'),  # Hotel Management View: Add
    path('hotel_image/', views.hotel_image_view, name='hotel_image'),  # Hotel Management View: View, Modify, Delete
]
