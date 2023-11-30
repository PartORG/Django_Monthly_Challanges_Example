from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name='index'),  # /challenges/
    path("<int:month>", views.monthly_challenge_by_number),  # placeholder (dynamic path), type of value will be checked for a number and converted to int.
    path("<str:month>", views.monthly_challenge, name="month-challenge"),  # placeholder (dynamic path), type of value will be checked for a str and converted to str.
]
