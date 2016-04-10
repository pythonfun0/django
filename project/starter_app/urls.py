from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.content_from_json, name='content_from_json'),
    # url(r'^$', views.home, name='home'),
]
