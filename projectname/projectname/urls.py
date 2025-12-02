from app import views
print("entry to urls.py")
"""
URL configuration for projectname project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
    # path('',views.landingpage,name='landingpage'),
   #path('landingpage',views.landingpage,name='landingpage'),
    #path('landingpage/',views.landingpage,name='landingpage'),
    #path('text_response/',views.text_response,name='text_response'),
   # path('html_response/',views.html_response,name='text-response'),
   #path('my_render/',views.my_render,name='my_render')
   #dynamic url
   #path('my_render/<str:x>/',views.my_render,name='my_render')
   #path('my_render/<str:name>/<int:age>/<str:quali>/',views.my_render,name='my_render'),
   #path('my_json/',views.my_json,name='my_json'),
   path('my_redirect/',views.my_redirect,name='my_redirect'),
   
]  

print("exit from urls.py")