from django.urls import path
from .views import index, searchProfesional, detailProfesional

from . import views

app_name = "core"

urlpatterns =[
    path('', index.as_view(), name="home"),
    path('search/', searchProfesional, name="search"),
    path('detail/<id>', detailProfesional, name="detailProfesional")
]