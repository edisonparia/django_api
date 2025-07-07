from django.urls import path
from .views import items_view

urlpatterns = [
    path('', items_view),
]
