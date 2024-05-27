from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("create_lead/<client_id>/",views.create_lead, name="create_lead" ),
    path("privacy_policy", views.privacy_policy, name="privacy_policy") ,
    #test : will be removed in production 
    path("testenv/", views.testenv, name="testenv"),
]
