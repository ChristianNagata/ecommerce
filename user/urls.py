from django.urls import path
from django.urls.conf import include
from . import views
from django.contrib.auth import login


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('logout/', views.logout_view, name='logout_view'),
    path('register/', views.register, name='register'),
]
