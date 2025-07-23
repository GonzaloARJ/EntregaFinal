from django.urls import path
from .views import userRegisterView, CustomLoginView, CustomLogoutView, ProfileView, AvatarUpdateView, ProfileUpdateView

urlpatterns = [
    path('register/', userRegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('update-profile/', ProfileUpdateView.as_view(), name='update-profile'),
    path('update-avatar/', AvatarUpdateView.as_view(), name='update-avatar'),
]