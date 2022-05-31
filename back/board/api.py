from http.client import UNAUTHORIZED, UNPROCESSABLE_ENTITY
from django.views import View
from django.http import Http404,  JsonResponse
from django.forms.models import model_to_dict
from board.httpResponse import HttpError
from board.models import User, Region
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime


def get_user_info(request, user_id):
    if request.method == "GET":
        if user_id:
            user_obj = User.objects.get(user_id=user_id)
            user = {
                "register": user_obj.register,
                "region": user_obj.region.name,
                "user_name": user_obj.user_name
            }
        return JsonResponse({"user":  user}, json_dumps_params={"ensure_ascii": False})
    return HttpError("NotFound", 404).send()

# 사용자 유저


class UserController(View):
    def post(self, request, *args, **kwargs):
        if "id" in request.session:
            user_id = request.session["id"]
            user = model_to_dict(User.objects.get(user_id=user_id))
            del user["salt"]
            del user["certification"]
        return JsonResponse({"user": user}, json_dumps_params={"ensure_ascii": False})


# 로그인 하면 나오는 개인정보 창
class AuthController(View):
    def get(self, request, *args, **kwargs):
        isSIgned = False
        obj = None
        if "id" in self.request.session:
            isSIgned = True
            obj = {
                "id": request.session["id"],
                "name": request.session["name"],
            }
        return JsonResponse({"isSigned": isSIgned, "user": obj}, json_dumps_params={"ensure_ascii": False})

    def post(self, request, *args, **kwargs):
        post = self.request.POST
        if not("id" in post and "pwd" in post):
            return HttpError("UNPROCESSABLE_ENTITY", UNPROCESSABLE_ENTITY).send()
        try:
            user = User.objects.get(user_id=post.get("id"))
            if check_password(post.get("pwd"), user.certification):
                self.request.session["id"] = user.user_id
                self.request.session["region"] = user.region.name
                self.request.session["name"] = user.user_name
                obj = {
                    "id": user.user_id,
                    "name": user.user_name,
                }
                return JsonResponse({"isSigned": True, "user": obj})
            return HttpError("UNAUTHORIZED", UNAUTHORIZED).send()
        except:
            return HttpError("UNAUTHORIZED", UNAUTHORIZED).send()

    # Sign out
    def delete(self, request, *args, **kwargs):
        for key in list(self.request.session.keys()):
            del request.session[key]
        return JsonResponse({})


# 회원가입
def Register(request):
    post = request.POST
    if not("id" in post, "user_name" in post, "phone" in post, "region" in post, "pwd" in post):
        return HttpError("UNPROCESSABLE_ENTITY", UNPROCESSABLE_ENTITY)
    user = User.objects.filter(user_id=post.get('id'))
    if(user.__len__() != 0):
        return HttpError("CONFLICT", 409).send()
    region, _ = Region.objects.get_or_create(name=post.get("region"))
    pwd = make_password(post.get("pwd"))
    user = User(
        user_id=post.get("id"),
        user_name=post.get("user_name"),
        register=datetime.today(),
        phone=post.get("phone"),
        region=region,
        certification=pwd
    )
    user.save()
    return JsonResponse({"result": "success"}, json_dumps_params={"ensure_ascii": False})
