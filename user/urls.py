from django.urls import path
from .views import UserProfileListCreate

urlpatterns = [
    path('profiles/', UserProfileListCreate.as_view()),
]
