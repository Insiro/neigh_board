from django.urls import path
from . import api

urlpatterns = [
    path("user/<str:user_id>", api.get_user_info),
    path("user/", api.UserController.as_view()),
    path("auth", api.AuthController.as_view()),

]
