from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import User


class UserController(View):
    def post(self, request, *args, **kwargs):

        pass

    def get(self, request):

        pass


class AuthController(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class Register(View):
    def post(self, request, *args, **kwargs):
        pass


class Region(View):
    def get(self, request, *args, **kwargs):
        pass

    def get(self, request, *args, **kwargs):
        pass
