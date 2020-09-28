from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('', views.account_view, name='account'),
    path('change_profile_photo', views.change_profile_photo_view, name='change_profile_photo'),
    path('add_profile_photo', views.add_profile_photo_view, name='add_profile_photo'),
    path('add_work', views.add_work_view, name='add_work'),
    path('like/<int:work_id>', views.like_view, name='like'),
    path('comment/<int:work_id>', views.comment_view, name='comment'),
    path('home', views.home, name='home'),
]
