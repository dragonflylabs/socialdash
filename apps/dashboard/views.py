from django.http import JsonResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View


class RegisterView(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(RegisterView, self).dispatch(*args, **kwargs)


    def get(self, request):
        return render_to_response('accounts/template_register.html', context_instance=RequestContext(request))


    def post(self, request):
        data = {
            'message': "ok"
        }
        return JsonResponse(data)


class LoginView(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(RegisterView, self).dispatch(*args, **kwargs)


    def get(self, request):
        return render_to_response('accounts/template_register.html', context_instance=RequestContext(request))


    def post(self, request):
        data = {
            'message': "ok"
        }
        return JsonResponse(data)