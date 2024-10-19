# chatbot/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Add this line for the home view
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('learn/', views.learn_view, name='learn'),
    path('about/', views.about_view, name='about'),
    path('practice/', views.practice_view, name='practice'),

]
