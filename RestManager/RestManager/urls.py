from django.contrib import admin
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    url('admin/', admin.site.urls),
]
