from django.urls import path
from . import views


urlpatterns = [
    path('create', views.create_group_view, name='create_form'),
    path('<str:group_name>', views.group_view, name='group')
]
