from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('healthz/', views.healthz_view),
    path('', views.hello_world),
]
