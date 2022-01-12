"""studentinfo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from info import views

urlpatterns = [
    path('accounts/', admin.site.urls),
    path('create_student/', views.create_student, name='create_student'),
    path('', views.show_student, name='show_student'),
    path('academics_details/<int:id>',
         views.academics_details, name='academics_details'),
    path('update_student/<int:id>', views.update_student, name='update_student'),
    path('delete_student/<int:id>', views.delete_student, name='delete_student'),
    path('url_search/', views.url_search, name='url_search'),
    path('user_logout/', views.user_logout, name='user_logout'),



]
