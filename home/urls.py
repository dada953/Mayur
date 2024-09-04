from django.urls import path
from home.views import StudentView
urlpatterns = [
    path('register/',StudentView.as_view(),name='register')
]
