from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search", views.search_entry, name="search_entry"),
    path("add", views.add, name="add"),
    path("wiki/<str:title>/edit", views.edit, name="edit"),
    path("random", views.random_entry, name="random")
]
