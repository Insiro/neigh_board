from django.views import View
from django.http import Http404, JsonResponse
from django.forms.models import model_to_dict
from board.models import User


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


class UserController(View):
    def post(self, request, *args, **kwargs):
        if "id" in request.session:
            user_id = request.session["id"]
            user = model_to_dict(User.objects.get(user_id=user_id))
            del user["salt"]
            del user["certification"]
        return JsonResponse({"user": user}, json_dumps_params={"ensure_ascii": False})


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


class Register(View):
    def post(self, request, *args, **kwargs):
        pass


class RegionController(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass
