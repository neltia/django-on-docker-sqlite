from django.urls import path
from service import views

urlpatterns = [
    path('', views.menu1, name="menu1_view"),
]
