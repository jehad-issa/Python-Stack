from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.show_form),
    path('register',views.register),
    path('login',views.login),
    path('success',views.success),
    path('clear',views.clear)

]