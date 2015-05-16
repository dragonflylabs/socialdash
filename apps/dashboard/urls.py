from django.conf.urls import patterns, include, url
from apps.dashboard.views import RegisterView, LoginView

urlpatterns = patterns('apps.gastalon_core.views',
    url(r'^$','home')
)