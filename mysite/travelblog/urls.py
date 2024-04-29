from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (HomeView, PostDetailView, ActivityDetailView, register, MyHomeView, PostCreateView, PostEditView,
                    PostDeleteView, ActivityCreateView, ActivityUpdateView, ActivityDeleteView)


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('activity/<int:pk>/', ActivityDetailView.as_view(), name='activity_detail'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='travelblog/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('myhome/', MyHomeView.as_view(), name='myhome'),
    path('add_post/', PostCreateView.as_view(), name='add_post'),
    path('post/edit/<int:pk>/', PostEditView.as_view(), name='edit_post'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='delete_post'),
    path('activity/add/', ActivityCreateView.as_view(), name='add_activity'),
    path('activity/edit/<int:pk>/', ActivityUpdateView.as_view(), name='edit_activity'),
    path('activity/delete/<int:pk>/', ActivityDeleteView.as_view(), name='delete_activity'),
]
