from django.template.defaultfilters import slugify
from django.shortcuts import render
import dateutil.parser
import datetime
import json
import os

from config.settings.base import DJANGO_ROOT
from .forms import CreateNewPost


json_file_path = os.path.join(DJANGO_ROOT, 'starter_app/static/data/blogs.json')


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


def posts(request):
    list_of_posts = {'posts': blog_data, 'details_of_post': None}
    return render(request, 'starter_app/home.html', list_of_posts)


def post_detail(request, slug):
    details = {'details_of_post': post_get_by_slug(slug), 'posts': blog_data}
    return render(request, 'starter_app/post_detail.html', details)


blog_data = read_data()


def create_new_post(request):
    message = ''
    form = CreateNewPost()
    title = None
    slug = None
    date_of_creation = None
    content = None
    created = False
    if request.method == 'POST':
        form = CreateNewPost(request.POST)
        if form.is_valid():
            created = True
            cd = form.cleaned_data
            title = cd['title']
            slug = slugify(cd['title'])
            date_of_creation = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            content = cd['content']
            message = "The new post was successfully saved!"

            new_post = {'title':title, 'slug':slug, 'published': date_of_creation, 'body': content}
            with open(json_file_path) as read_json:
                data = json.load(read_json)
           
            data.append(new_post)

            with open(json_file_path, 'w') as write_json:
                json.dump(data, write_json, sort_keys=True, indent=4, ensure_ascii=False)

    return render(request, 'starter_app/create_new_post.html', {'posts': blog_data,
                                                                'details_of_post': None,
                                                                'message': message,
                                                                'form': form,
                                                                'title': title,
                                                                'slug': slug,
                                                                'date_of_creation': date_of_creation,
                                                                'content': content,
                                                                'created': created})
