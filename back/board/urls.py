from django.urls import path

from board import post_api
from . import api

urlpatterns = [
    path("user/<str:user_id>", api.get_user_info),
    path("user", api.UserController.as_view()),
    path("auth", api.AuthController.as_view()),
    path("comment/<str:id>", post_api.CommentController.as_view()),
    path("register", api.Register),


    path("post", post_api.PostController.as_view()),
    path("post/<str:id>", post_api.PostItemController.as_view()),
    path("comment", post_api.CommentController.as_view())
]
