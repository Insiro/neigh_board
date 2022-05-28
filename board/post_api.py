from django.views import View
from django.http import Http404, JsonResponse
from django.forms.models import model_to_dict
from board.models import Post

class PostController(View):
    def post(self, request, *args, **kwargs):
        new_board = {
            "board_id" : request.session['board_id'],
            "author" : request.session['author'],
            "title" : request.session['title'],
            "content" : request.session['content'],
            "likes" : request.session['likes'],
            "region" : request.session['region'],
            "date" : request.session['date']
        }
        return JsonResponse({"post_board" : new_board}, json_dumps_params={"ensure_ascii" : False})
        

    def get(self, request, *args, **kwargs):
        all_board = model_to_dict(Post.objects.all) # 게시판 전체 다 보여주기
        return JsonResponse({"board" : all_board}, json_dumps_params={"ensure_ascii" : False})


class CommentController(View):
    def post(self, request, *args, **kwargs):
        pass

    def get(self, request, *args, **kwargs):
        pass
    