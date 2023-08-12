from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Define a URL pattern for the root path
]