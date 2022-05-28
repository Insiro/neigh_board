from django.urls import path

from . import post_api
from . import api

# 클래스형 뷰는 클래스로 진입하기 위한 as_view() 클래스 메소드로 진입메소드라 부름
# 클래스형 뷰에는 내부적으로 dispatch() 메소드가 있기 때문에 
#dispatch()메소드가 get,post등의 어떤 HTTP 메소드로 요청을 중계해줌

# 제네릭 뷰를 상속받아서 클래스형 뷰를 만들기 위하여 urlspatterns에 .as_view( )를 호출
urlpatterns = [
    path("user/<str:user_id>", api.get_user_info),
    path("user/", api.UserController.as_view()),
    path("auth", api.AuthController.as_view()),
    #pk(int) 번째 자원에 추가
    path('new_comment/<int:post_id>', post_api.CommentController.as_view())
]
