from django.urls import path
from .views import LoginView, SignUpView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('signup/', SignUpView.as_view()),
]