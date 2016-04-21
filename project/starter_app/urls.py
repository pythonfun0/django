from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.blogs, name='blogs'),
	url(r'^blogs/(?P<slug>.+)/$', views.post_detail, name='post detail'),
]
