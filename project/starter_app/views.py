from django.template.defaultfilters import slugify
from django.shortcuts import render
from datetime import datetime
import json
import os

from config.settings.base import DJANGO_ROOT
# from .models import Message

json_file_path = os.path.join(DJANGO_ROOT, 'data', 'blogs.json')


with open(json_file_path) as from_json:
        loaded_data = json.load(from_json)
from_json.close()


for item in loaded_data:
    loaded_data[item]['published'] = eval(loaded_data[item]['published'])
    loaded_data[item]['slug'] = slugify(loaded_data[item]['title'])


def blogs(request):
    list_of_blogs = {'blogs': loaded_data}
    return render(request, 'starter_app/home.html', list_of_blogs)


def post_detail(request):
    slug = str(request)[20:-2]
    for item in loaded_data.keys():
        if loaded_data[item]['slug'] == slug:
            details = {'details_of_blogs': loaded_data[item]}
    return render(request, 'starter_app/post_detail.html', details)


# counter = 0
# relode_counter = -1
# with open(json_file_path) as from_json:
#         loaded_data = json.load(from_json)['new blog content']
#         # counter += 1
# from_json.close()
# 
# 
# def content_from_json(request):
#     global relode_counter
#     relode_counter += 1
#     text = {
#         'json_data': loaded_data,
#         'loaded_num': 'The json file was loaded only at %s!' % counter,
#         'relode_counter': 'The page was reloded: %s ' % relode_counter
#     }
#     return render(request, 'starter_app/home.html', text)


# def home(request):
#     messages = Message.objects.order_by('order')
#     messages = ['1st', '2nd', '3th']
#     context_dict = {
#         'messages': messages
#     }
#     return render(request, 'starter_app/home.html', context_dict)
