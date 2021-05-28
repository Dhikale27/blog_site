from django.urls import path
from .views import SingUpView


app_name = 'basic_app'

urlpatterns = [
    path('sign_up', SingUpView.as_view(), name="sing_up")
]
