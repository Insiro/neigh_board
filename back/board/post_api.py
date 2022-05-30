from datetime import datetime
from http.client import UNAUTHORIZED, UNPROCESSABLE_ENTITY
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import check_password
from django.forms.models import model_to_dict
from board.httpResponse import HttpError
from board.models import Post, Comment, User, Region
import json


class PostController(View):
    def post(self, request, *args, **kwargs):
        if not "id" in request.session:
            return HttpError("UNAUTHORIZED", UNAUTHORIZED)
        body = json.loads(request.body)
        user_id = self.request.session["id"]
        author = User.objects.get(user_id=user_id)
        region = Region.objects.get(name=request.session['region'])
        Post.objects.create(
            author=author,
            region=region,
            title=body.get("title"),
            content=body.get("content"),
            likes=0,
            date=datetime.today()
        ).save()
        return JsonResponse({"result": "success"}, json_dumps_params={"ensure_ascii": False})

    def get(self, request, *args, **kwargs):
        all_post = []
        if "all" in self.request.GET:
            all_post = Post.objects.all()  # 게시판 전체 다 보여주기
        elif "region" in self.request.session:
            all_post = Post.objects.filter(
                region=self.request.session["region"])

        posts = []
        for item in all_post:
            post = model_to_dict(item)
            post["id"] = item.board_id
            posts.append(post)
        return JsonResponse({"posts": posts}, json_dumps_params={"ensure_ascii": False})


class PostItemController(View):
    def dispatch(self, request, *args, **kwargs):
        self.id = kwargs["id"]
        try:
            self.post = Post.objects.get(board_id=kwargs["id"])
            return super().dispatch(request, args, kwargs)
        except:
            return HttpResponse("NOTFOUND", status=404)

    def delete(self, request, *args, **kwargs):
        body = json.loads(request.body)
        try:
            if not "pwd" in body or not "id" in request.session:
                raise HttpError("UNAUTHORIZED", UNAUTHORIZED)
            if not check_password(body.get("pwd"), self.post.author.certification):
                raise HttpError("UNAUTHORIZED", UNAUTHORIZED)
            self.post.delete()
            return HttpResponse("success")
        except HttpError as error:
            error.send()
        except ObjectDoesNotExist:
            return HttpResponse("NOTFOUND", status=404)

    def get(self, request, *args, **kwargs):
        return JsonResponse({"post": model_to_dict(self.post)}, json_dumps_params={"ensure_ascii": False})


class PostCommentItems(View):
    def dispatch(self, request, *args, **kwargs):
        self.post_id = kwargs["post_id"]
        try:
            self.posts = Post.objects.get(board_id=self.post_id)
            return super().dispatch(request, args, kwargs)
        except ObjectDoesNotExist:
            return HttpResponse("NOTFOUND", status=404)

    def get(self, request, *args, **kwargs):
        comment_list = Comment.objects.filter(post=self.posts)
        comments = []
        for item in comment_list:
            post = model_to_dict(item)
            post["id"] = item.comment_id
            comments.append(post)
        return JsonResponse({"comments": comments}, json_dumps_params={"ensure_ascii": False})

    def post(self, request, *args, **kwargs):
        body = json.loads(request.body)
        try:
            if not "id" in request.session:
                raise HttpError("UNAUTHORIZED", UNAUTHORIZED)
            if not "comment" in body:
                raise HttpError("UNPROCESSABLE_ENTITY", UNPROCESSABLE_ENTITY)
            if not "comment" in body:
                raise HttpError("UNPROCESSABLE_ENTITY", UNPROCESSABLE_ENTITY)
            user = User.objects.get(user_id=request.session["id"])
            Comment.objects.create(
                post=self.posts,
                author=user,
                comment=body["comment"],
                date=datetime.now()
            )
            return HttpResponse("success")
        except HttpError as e:
            e.send()


class CommentController(View):
    def dispatch(self, request, *args, **kwargs):
        self.id = kwargs.get("id")
        try:
            self.coms = Comment.objects.get(comment_id=self.id)
            return super().dispatch(request, args, kwargs)
        except ObjectDoesNotExist:
            return HttpResponse("NOTFOUND", status=404)

    def get(self, request, *args, **kwargs):
        return JsonResponse({"comment": model_to_dict(self.coms)}, json_dumps_params={"ensure_ascii": False})
