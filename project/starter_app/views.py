from django.template import RequestContext
from django.shortcuts import render
import dateutil.parser
import json
import os

from config.settings.base import DJANGO_ROOT


def read_data():
    json_file_path = os.path.join(DJANGO_ROOT, 'starter_app/static/data/blogs.json')

    with open(json_file_path) as blog_json:
        blog_data = json.load(blog_json)

    for item in blog_data:
        item['published_datetime'] = dateutil.parser.parse(item['published'])
    return blog_data


def post_get_by_slug(slug):
    for item in blog_data:
        if item['slug'] == slug:
            details = item
    return details


def blogs(request):
    list_of_posts = {'posts': blog_data}
    return render(request, 'starter_app/home.html', list_of_posts)


def post_detail(request, slug):
    details = {'details_of_post': post_get_by_slug(slug), 'posts': blog_data}
    return render(request, 'starter_app/post_detail.html', details)


blog_data = read_data()
