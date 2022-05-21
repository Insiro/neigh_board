from django.urls import path
from . import views

urlpatterns = [
    path("user", views.UserController.as_view),
    path("auth", views.AuthController.as_view),

]
