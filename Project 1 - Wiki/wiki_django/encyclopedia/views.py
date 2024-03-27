from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import random

from . import util

class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content", widget=forms.Textarea)

class EditEntryForm(forms.Form):
    content = forms.CharField(label="Content", widget=forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    if content == None:
        return render(request, "encyclopedia/error_404.html")
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": content
        })

def search_entry(request):
    query = request.GET.get('q', '')

    if query in util.list_entries():
        return HttpResponseRedirect(reverse("wiki:entry", kwargs={'title': query}))

    else:
        list_result = [entry for entry in util.list_entries() if query in entry]
        return render(request, "encyclopedia/search_entry.html", {
            "search": query,
            "entries": list_result
        })

def add(request):
    if request.method == 'POST':
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            if title not in util.list_entries():
                content = form.cleaned_data["content"]
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse("wiki:entry", kwargs={'title': title}))
            else:
                return render(request, "encyclopedia/add.html", {
                    "form": form,
                    "error": True
                })

        else:
            return render(request, "encyclopedia/add.html", {
                "form": form,
                "error" : False
            })

    return render(request, "encyclopedia/add.html", {
        "form": NewEntryForm(),
        "error" : False
    })

def edit(request, title):
    if request.method == 'POST':
        form = EditEntryForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("wiki:entry", kwargs={'title': title}))

        else:
            return render(request, "encyclopedia/edit.html", {
                "title": title,
                "form": form
            })

    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "form": EditEntryForm()
    })

def random_entry(request):
    title = random.choice(util.list_entries())
    return HttpResponseRedirect(reverse("wiki:entry", kwargs={'title': title})) 