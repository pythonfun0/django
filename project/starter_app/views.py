from django.shortcuts import render
import json
import os
# from .models import Message


module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'data.json')


counter = 0
relode_counter = -1
with open(file_path) as from_json:
        loaded_data = json.load(from_json)['new blog content']
        counter += 1
from_json.close()


def content_from_json(request):
    global relode_counter
    relode_counter += 1
    text = {
        'json_data': loaded_data,
        'loaded_num': 'The json file was loaded only at %s!' % counter,
        'relode_counter': 'The page was reloded: %s ' % relode_counter
    }
    return render(request, 'starter_app/home.html', text)


# def home(request):
#     messages = Message.objects.order_by('order')
#     messages = ['1st', '2nd', '3th']
#     context_dict = {
#         'messages': messages
#     }
#     return render(request, 'starter_app/home.html', context_dict)
