from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),  # members
    path('member/<int:id>/', views.details, name='details'),  # member details
]