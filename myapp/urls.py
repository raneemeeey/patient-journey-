
from django.urls import path
from . import views


urlpatterns = [

    # Home page
    path(
        "",
        views.home,
        name="home"
    ),

    # Plastic Surgery
    path(
        "subspecialties/<str:specialty_slug>/",
        views.subspecialties,
        name="subspecialties"
    ),

    # Hand Surgery
    path(
        "surgeries/<str:subspecialty_slug>/",
        views.surgeries,
        name="surgeries"
    ),

    # Individual Surgery
    path(
        "surgery/<str:surgery_slug>/",
        views.surgery_detail,
        name="surgery_detail"
    ),

]
