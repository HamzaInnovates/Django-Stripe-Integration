from django.urls import path
from .views import home, success, cancel

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('success/', success, name='success'),  # Success page after payment
    path('canceled/', cancel, name='cancel'),  # Canceled page
]
