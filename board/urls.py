from django.urls import path
from . import api, post_api

# urls.py는 사용자가 보낸 request의 url을 확인하는 역할을 한다.
urlpatterns = [
    path("user/<str:user_id>", api.get_user_info),
    path("user/", api.UserController.as_view()),
    path("auth", api.AuthController.as_view()),
    path("region_post", api.RegionController.as_view()),
    path("register", api.Register.as_view()),
    path("isSigned", api.AuthController.as_view()),
    path("post_board", post_api.PostController.as_view()),
    path("board", post_api.PostController.as_view())
]
