from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("test", views.test, name="test"),
    path("card", views.card, name="card"),
]