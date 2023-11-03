from django.urls import path
from .views import home,create,edit,delete

urlpatterns = [
    path("",home,name='home'),
    path("create/",create,name='create'),
    path("edit/<int:pk>/",edit,name='edit'),
    path("delete/<int:pk>/",delete,name='delete')
]