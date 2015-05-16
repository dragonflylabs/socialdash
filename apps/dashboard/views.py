#-*- coding: utf-8 -*-
import json
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import View


class LoginView(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)

    def get(self, request):
        return render_to_response('dashboard/template_account.html', context_instance=RequestContext(request))

@csrf_exempt
@require_POST
def register_user(request):
    data = json.loads(request.body)
    try:
        email = data.get('email', None)
        password = data.get('password', None)
        password_confirm = data.get('password2', None)
        if email and password and password_confirm:
            if password.strip() == password_confirm.strip():
                if User.objects.filter(email=email).count():
                    return JsonResponse(json.loads({'status': 400, 'msg': 'El usuario ya existe'}))
                else:
                    user = User()
                    user.email = email
                    user.set_password(password)
                    user.save()
                    return JsonResponse(json.loads({'status': 200, 'msg': 'El usuario fue creado con éxito'}))
            else:
                return JsonResponse(json.loads({'status': 400, 'msg': 'Las contraseñas no coinciden'}))
        else:
            return JsonResponse(json.loads({'status': 400, 'msg': 'Los campos son obligatorios'}))
    except Exception as e:
        return JsonResponse(json.loads({'status': 400, 'msg': e.message}))
        pass

@csrf_exempt
@require_POST
def login_user(request):
    data = json.loads(request.body)
    try:
        email = data.get('email', None)
        password = data.get('password', None)
        if email and password:
            if User.objects.filter(email=email).count():
                return JsonResponse(json.loads({'status': 400, 'msg': 'El usuario ya existe'}))
            else:
                return JsonResponse(json.loads({'status': 400, 'msg': 'El usuario ya existe'}))
        else:
            return JsonResponse(json.loads({'status': 400, 'msg': 'Los campos son obligatorios'}))
    except Exception as e:
        pass
    return JsonResponse(data)

def home(request):
    return render_to_response('dashboard/template_home.html', context_instance=RequestContext(request))