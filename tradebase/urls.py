from django.urls import path
from . import views

urlpatterns = [
    path('', views.tradebase_home, name="tbHome"),
    path('userdetails/', views.user_detials, name="userdetails"),
]