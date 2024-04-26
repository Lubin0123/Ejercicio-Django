
from django.contrib import admin
from django.urls import path
from lubin.views import indexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',indexView)
]
