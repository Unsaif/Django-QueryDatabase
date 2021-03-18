from django.urls import path
from . import views

urlpatterns = [
    path('', views.JoinFormView.as_view(), name = "JoinFormView")
]