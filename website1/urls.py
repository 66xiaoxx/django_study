"""website1 URL Configuration

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
from django.urls import path, re_path
from django.conf.urls import url
from django.views.static import serve
from  webpage import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.main),
    # path('login/main.html', views.main),
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', views.register),
    path('系统管理_用户管理/',views.sysuser),
    path('系统管理_用户管理/adduser/',views.adduser),
    path('系统管理_角色管理/',views.sysrole),
    path('系统管理_机构管理/', views.sysorg),
    path('系统管理_菜单管理/', views.sysmenu),
    path('系统管理_按钮管理/', views.sysbottom),
    path('系统管理_数据字典/', views.param),
    path('templates/<path:path>)', serve, {'document_root': '/templates'}),
    path('templates/login/<path:path>)', serve, {'document_root': '/templates/login'}),
    path('login/<path:path>)', serve, {'document_root': '/templates/login'}),
    path('static/<path:path>)', serve, {'document_root': '/static'}),
    path('static/css/<path:path>)', serve, {'document_root': '/static/css'}),
    path('static/css/icons/<path:path>)', serve, {'document_root': '/static/css/icons'}),
    path('static/css/images/<path:path>)', serve, {'document_root': '/static/css/images'}),
    path('static/js/<path:path>)', serve, {'document_root': '/static/js'}),
    path('static/v2.0/<path:path>)', serve, {'document_root': '/static/v2.0'}),
    path('static/v2.0/css/<path:path>)', serve, {'document_root': '/static/v2.0/css'}),
    path('static/v2.0/data/<path:path>)', serve, {'document_root': '/static/v2.0/data'}),
    path('static/v2.0/fonts/<path:path>)', serve, {'document_root': '/static/v2.0/fonts'}),
    path('static/v2.0/images/<path:path>)', serve, {'document_root': '/static/v2.0/images'}),
    path('static/v2.0/js/<path:path>)', serve, {'document_root': '/static/v2.0/js'}),
    path('static/v2.0/uplanPlug/<path:path>)', serve, {'document_root': '/static/v2.0/uplanPlug'}),
]
