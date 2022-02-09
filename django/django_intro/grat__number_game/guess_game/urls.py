from pydoc import visiblename
from django.urls import path

from . import views

urlpatterns = [
    path('', views.guess_game)
]
