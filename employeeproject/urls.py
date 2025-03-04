"""
URL configuration for employeeproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from employeeapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name="home_view"),
    path('reg',views.RegisterView.as_view(),name="reg_view"),
    path('list',views.Employeelist.as_view(),name="emp_list"),
    path('del/<int:id>',views.DeleteEmployee.as_view(),name="delete_view"),
    path('update/<int:id>',views.UpdateEmployee.as_view(),name="update_view")

]
