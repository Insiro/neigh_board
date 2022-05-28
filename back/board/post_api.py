from django.shortcuts import get_object_or_404
from audioop import reverse
from django.shortcuts import redirect, render
from django.views import View
from django.http import Http404, JsonResponse
from django.forms.models import model_to_dict

from neigh_board.back.board.models import User, Comment, Post, Region

class PostController(View):
    def post(self, request, *args, **kwargs):
        pass

    def get(self, request, *args, **kwargs):
        pass


# request.session == 현재 서비스를 이용하고 있는 사람의 정보
class CommentController(View):
    def post(self, request, *args, **kwargs): 
        #댓글 객체를 만들어주는 역할
        errors=[]
        if "comment_id" in request:
            comment_id = request["comment_id"]
            comment = model_to_dict(Comment.objects.get(comment_id=comment_id))
        return JsonResponse({"new_comment": comment}, json_dumps_params={"ensure_ascii": False})
        

    def get(self, request, *args, **kwargs): # 댓글을 보여주는 코드, 해당 게시물의 post_id만 갖는 댓글만 필터링하여 저장하고 
        #comment.post == board.board_id
        if kwargs.get('board_id') is None:
            comment_queryset = Comment.objects.all() #모든 comment의 정보를 불러온다.
            return JsonResponse({"board": comment_queryset}, json_dumps_params={"ensure_ascii": False})
        else:
            board_id = kwargs.get('board_id')
            comment_queryset = Comment.objects.all(Comment.objects.get(post=board_id)) #id에 해당하는 User의 정보를 불러온다
            return JsonResponse({"board": comment_queryset}, json_dumps_params={"ensure_ascii": False})
        


