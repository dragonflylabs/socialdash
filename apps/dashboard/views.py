from django.http import JsonResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View


class LoginView(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)


    def get(self, request):
        return render_to_response('dashboard/template_account.html', context_instance=RequestContext(request))


    def post(self, request):
        data = {
            'message': "ok"
        }
        return JsonResponse(data)


def home(request):
    return render_to_response('dashboard/template_home.html', context_instance=RequestContext(request))