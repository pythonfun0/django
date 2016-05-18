from django.conf.urls import url
from . import views


app_name = 'starter_app'
urlpatterns = [
	url(r'^home/$', views.posts, name='posts'),
	url(r'^posts/(?P<slug>.+)$', views.post_detail, name='post_detail'),
	url(r'^create-new-post/$', views.create_new_post, name='create_new_post'),
]
