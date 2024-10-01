from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="home"),
    path('delete_user/<int:id>', delete_user, name="delete_user")
]
