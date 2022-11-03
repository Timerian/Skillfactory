from django.urls import include, path

from project.accounts.views import SignUp

urlpatterns = [
    path('signup', SignUp.as_view(), name='signup'),
]