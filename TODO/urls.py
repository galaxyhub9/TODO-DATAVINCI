"""
URL configuration for TODO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from todoApp.views import get_tasks, update_tasks, add_task, delete_tasks, api_overview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_overview),
    path(r'get/tasks/', get_tasks),
    path(r'post/tasks/', add_task,),
    path(r'put/tasks/<int:id>/',update_tasks),
    path(r'delete/tasks/<int:id>/',delete_tasks),
]
