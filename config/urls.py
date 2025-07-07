from django.urls import path, include

urlpatterns = [
    path('items/', include('items.urls')),
]
