from django.urls import path, include
from django.shortcuts import render
from .views import HomePageView, AboutPageView#, PasswordChangeDoneView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name='about'),
 #   path('password/change/done', PasswordChangeDoneView.as_view(), name='password_change_done'),
]