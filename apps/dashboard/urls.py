from django.conf.urls import patterns, include, url
from apps.dashboard.views import LoginView

urlpatterns = patterns('apps.dashboard.views',
    url(r'^$', 'home'),
    url(r'^login/$', LoginView.as_view()),
)