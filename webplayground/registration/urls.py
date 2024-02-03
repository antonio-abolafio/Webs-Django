from django.urls import path
from .views import SignUpView, ProfileUpdateView, EmailUpdate

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('profile/email/', EmailUpdate.as_view(), name='profile_email')
]
