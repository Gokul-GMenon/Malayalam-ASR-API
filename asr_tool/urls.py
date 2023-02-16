from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home),
    path('post', views.predict),
]