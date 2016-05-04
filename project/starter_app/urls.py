from django.conf.urls import url
from . import views


app_name = 'starter_app'
urlpatterns = [
	url(r'^posts/$', views.blogs, name='blogs'),
	url(r'^posts/(?P<slug>.+)/$', views.post_detail, name='post_detail'),
]
