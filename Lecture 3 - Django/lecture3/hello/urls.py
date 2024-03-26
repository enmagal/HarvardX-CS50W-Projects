from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("enzo", views.enzo, name="enzo"),
    path("agathe", views.agathe, name="agathe")
]