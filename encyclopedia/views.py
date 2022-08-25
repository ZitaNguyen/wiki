from django.shortcuts import render

from . import util

import markdown
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    content = util.get_entry(title)

    # check if entry exists before converting markdown into html
    if content:
        content = markdown.markdown(content, output_format='html5')

    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": content
    })


def search(request):
    if request.method == 'GET':

        entries = [entry.lower() for entry in util.list_entries()]
        query = request.GET.get('q').lower()

        # query matches the name of entry
        if query in entries:
            return entry(request, query)

        # query as a substring
        else:
            results = [entry for entry in entries if query in entry]
            return render(request, "encyclopedia/search.html", {
                "results": results
            })


def create_page(request):
    if request.method == 'POST':

        title = request.POST.get('title')
        content = request.POST.get('content')
        entries = [entry.lower() for entry in util.list_entries()]

        # if title already exists, return error message
        if title.lower() in entries:
            return render(request, "encyclopedia/create_page.html", {
                "message" : "This title already exists."
            })

        # if not, save new entry
        else:
            util.save_entry(title, content)
            return entry(request, title)

    else:
        return render(request, "encyclopedia/create_page.html", {
            "message" : ""
        })


def edit_page(request, title):
    if request.method == 'POST':
        
        title = request.POST.get('title')
        content = request.POST.get('content')
        util.save_entry(title, content)
        return entry(request, title)

    else:
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit_page.html", {
            "title" : title,
            "entry" : content
        })


def random_page(request):
    entries = util.list_entries()
    title = random.choice(entries)
    return entry(request, title)