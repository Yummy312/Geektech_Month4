from user.views import auth_view, logout_view, register_view
from django.urls import path
urlpatterns = [
    path('users/auth/', auth_view),
    path('users/logout/', logout_view),
    path('users/register/', register_view)
]