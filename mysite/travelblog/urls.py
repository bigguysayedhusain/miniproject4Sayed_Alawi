from django.urls import path
from .views import HomeView  # Adjust this import according to your project structure


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # Other URL patterns for your app
]
