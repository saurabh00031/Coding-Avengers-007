"""reg_main URL Configuration

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
from django.urls.conf import include

admin.site.site_header = "Dare_to_Care_health Admin"
admin.site.site_title = " hightech_health Admin Portal"
admin.site.index_title = "Welcome to Dare_to_care_health Researcher Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reg.urls')),
]
