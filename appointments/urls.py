from django.urls import path
from . import views
from authentication import views as authentication_views

urlpatterns = [
    path('', views.appointment, name='appointment'),
    path('my_appointments/', views.my_appointments, name='my_appointments'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('unbook_appointment/', views.unbook_appointment, name='unbook_appointment'),
]
