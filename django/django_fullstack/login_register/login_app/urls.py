from sre_constants import SUCCESS
from django.urls import path
from . import views


urlpatterns = [
    path('',views.form_page ),
    path('register',views.register),
    path('login',views.login),
    path('success',views.success),
]