from django.urls import path
from login_system import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name="home"),
]
