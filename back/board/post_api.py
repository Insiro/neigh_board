from datetime import datetime
from django.views import View
from django.http import Http404, HttpResponseBadRequest, JsonResponse
from django.forms.models import model_to_dict
from board.models import Post, Comment


class PostController(View):
    def post(self, request, *args, **kwargs):
        post = self.request.POST
        author = self.request.session["id"]
        Post(
            author=author,
            region=request.session['region'],
            title=post.get("title"),
            content=post.get("content"),
            likes=0,
            date=datetime.today()
        ).save()
        return JsonResponse({"result": "success"}, json_dumps_params={"ensure_ascii": False})

    def get(self, request, *args, **kwargs):
        if "region" in self.request.session:
            all_board = model_to_dict(Post.objects.filter(
                region=self.request.session["region"]))
        else:
            all_board = model_to_dict(Post.objects.all())  # 게시판 전체 다 보여주기
        return JsonResponse({"board": all_board}, json_dumps_params={"ensure_ascii": False})


class PostItemController(View):
    def delete(self, request, *args, **kwargs):
        pass

    def get(self, request, *args, **kwargs):
        pass


class CommentController(View):
    def post(self, request, args, **kwargs):
        # 댓글 객체를 만들어주는 역할
        post = self.request.POST
        if not("id" in kwargs and "comment" in post and "author" in post):
            return HttpResponseBadRequest()

        comment = Comment(post=kwargs["id"], comment=post.get("comment"),
                          author=post.get("author"), date=datetime.now())
        comment.save()

        return JsonResponse({"new_comment": comment}, json_dumps_params={"ensure_ascii": False})

    def get(self, request, args, **kwargs):  # 댓글을 보여주는 코드, 해당 게시물의 post_id만 갖는 댓글만 필터링하여 저장하고
        #comment.post == board.board_id
        comm_id = kwargs.get('id')
        if comm_id is None:
            comments = Comment.objects.filter(comment_id=comm_id)

            return JsonResponse({"board": model_to_dict(comments)}, json_dumps_params={"ensure_ascii": False})
        else:
            return Http404
