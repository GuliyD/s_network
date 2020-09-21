from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('', views.account_view, name='account'),
    path('register', views.create_user_view, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('login', views.login_view, name='login')
]
