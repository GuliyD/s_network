from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('', views.account_view, name='account'),
    path('register', views.create_user_view, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('login', views.login_view, name='login'),
    path('change_profile_photo', views.change_profile_photo_view, name='change_profile_photo'),
    path('add_profile_photo', views.add_profile_photo_view, name='add_profile_photo'),
    path('add_work', views.add_work_view, name='add_work'),
    path('like/<int:work_id>', views.like_view, name='like'),
    path('comment/<int:work_id>', views.comment_view, name='comment')
]
