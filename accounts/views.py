from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView,
    CreateView,
    UpdateView,

)

# Create your views here.
class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

class AboutPageView(LoginRequiredMixin, TemplateView):
    template_name = 'about.html'

# class PasswordChangeDoneView(LoginRequiredMixin, TemplateView):
#     template_name = 'password_change_done.html'