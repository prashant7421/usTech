from django.urls import path
from cricket.views import PlayerProfile

urlpatterns = [
    path('player_profile/<int:id>', PlayerProfile.as_view(), name='player_profile')
]
