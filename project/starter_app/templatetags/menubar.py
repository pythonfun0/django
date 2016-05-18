from django import template
from .. import views

register = template.Library()


@register.inclusion_tag('starter_app/navigation.html', takes_context=True)
def menubar(context):
	return { 'posts': context['posts'], 'details_of_post': context['details_of_post']}
