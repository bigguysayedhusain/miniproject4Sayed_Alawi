from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register
from .views import HomeView, PostDetailView, ActivityDetailView, MyHomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('activity/<int:pk>/', ActivityDetailView.as_view(), name='activity_detail'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='travelblog/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('myhome/', MyHomeView.as_view(), name='myhome'),
]
