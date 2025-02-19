from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='home'),  # members
    path('member/<int:id>/', views.details, name='details'),  # member details
    path('login/', views.login_user, name='login'),
    path('contact/', views.contact_form, name='contact-form'),
]