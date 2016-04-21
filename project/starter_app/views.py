from django.template.defaultfilters import slugify
from django.shortcuts import render
import datetime
import json
import os

from config.settings.base import DJANGO_ROOT


def blogs(request):
    global raw_data
    json_file_path = os.path.join(DJANGO_ROOT, 'data', 'blogs.json')

    with open(json_file_path) as blog_json:
        raw_data = json.load(blog_json)

    for item in raw_data:
        raw_data[raw_data.index(item)]['published'] = datetime.datetime( \
            item['published'][0], item['published'][1], item['published'][2], \
            item['published'][3], item['published'][4], item['published'][5])
        raw_data[raw_data.index(item)].update({"slug": slugify(item['title'])})

    list_of_blogs = {'blogs': raw_data}
    return render(request, 'starter_app/home.html', list_of_blogs)


def post_detail(request, slug):
    for item in raw_data:
        if item['slug'] == slug:
            details = {'details_of_blogs': item}
    return render(request, 'starter_app/post_detail.html', details)

