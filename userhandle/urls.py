from django.urls import path 
from . import views 


urlpatterns = [
    path("welcome-email", views.welcome_email, name="welcome-email"),
    path("client-login", views.client_login, name="client-login"), 
    path("client-registration", views.client_registration, name="client-registration"),
    path("client-logout", views.client_logout, name="client-logout"),
]