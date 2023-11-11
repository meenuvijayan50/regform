from django.urls import path
from .views import register_user, get_user_details

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('user/<int:user_id>/', get_user_details, name='get_user_details'),

]