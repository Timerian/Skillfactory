from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import SignUpForm


class SignUp(SignUpForm):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'
