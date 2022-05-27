from statistics import mode
from django.views import View
from django.http import Http404, JsonResponse
from django.forms.models import model_to_dict
from board.models import Region
from board.models import User, Post


def get_user_info(request, user_id):
    if request.method == "GET":
        if user_id:
            user_obj = User.objects.get(user_id=user_id)
            user = {
                "register": user_obj.register,
                "region": user_obj.region,
                "user_name": user_obj.user_name
            }
        return JsonResponse({"user": user}, json_dumps_params={"ensure_ascii": False})
    return Http404()


# 사용자 유저
class UserController(View):
    def post(self, request, *args, **kwargs):
        if "id" in request.session:
            user_id = request.session["id"]
            user = model_to_dict(User.objects.get(user_id=user_id))
            del user["salt"]
            del user["certification"]
        return JsonResponse({"user": user}, json_dumps_params={"ensure_ascii": False})


# 지역인증
class RegionController(View):
    def get(self, request, *args, **kwargs):
        isSigned = 'id' in self.request.session
        return JsonResponse({"isSigned": isSigned}, json_dumps_params={"ensure_ascii": False})
        
    def post(self, request, *args, **kwargs):
        if 'region' in request.session:
            user_region = request.session["region"]
            user = model_to_dict(Post.objects.get(user_region=user_region)) # Model 안에 region = request.session 으로 받은 region
        return JsonResponse({"Region_post" : user}, json_dumps_params={"ensure_ascii": False}) 
        

# 로그인 하면 나오는 개인정보 창
class AuthController(View):
    def get(self, request, *args, **kwargs):
        isSIgned = 'id' in self.request.session
        return JsonResponse({"isSigned": isSIgned}, json_dumps_params={"ensure_ascii": False})

    def post(self, request, *args, **kwargs):
        pass

    # Sign out
    def delete(self, request, *args, **kwargs):
        for key in list(self.request.session.keys()):
            del request.session[key]


# 회원가입
class Register(View):
    def post(self, request, *args, **kwargs):
        new_user = {
            'user_id' : request.session
        }