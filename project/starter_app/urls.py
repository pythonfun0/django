from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.blogs, name='blogs'),
	url(r'^.+$', views.post_detail, name='post detail'),
	# url(r'^$', views.content_from_json, name='content_from_json'),
	# url(r'^$', views.home, name='home'),
]
