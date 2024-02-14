from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('get_random_object', views.get_random_object, name='get_random_object')
]
