from django.urls import path
from . import views
from authentication import views as authentication_views

urlpatterns = [
    path('', views.appointment, name='appointment'),
]
