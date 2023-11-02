from django.urls import path
from .views import home,create,edit

urlpatterns = [
    path("",home,name='home'),
    path("create/",create,name='create'),
    path("edit/<int:pk>/",edit,name='edit')
]