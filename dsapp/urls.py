from django.urls import path
from . import views

urlpatterns = [
    path('homepage',views.home),
    path('modelform',views.modelform)
]