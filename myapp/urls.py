from django.urls import path
from .views import home,search

urlpatterns = [
    path('',home, name="index"),
    path('place/',search,name="search")
]