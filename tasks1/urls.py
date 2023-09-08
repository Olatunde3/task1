from django.urls import path
from . import views


urlpatterns = [
    path("slack_name=olatunde&track=backend", views.getData, name="home")
]
