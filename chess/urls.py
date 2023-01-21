from django.urls import path

from .views import ChessIndex, ChessPlayerSignup, ChessPlayerDashboard
from .authenticaion import user_required

urlpatterns = [
    path('', ChessIndex.as_view(), name="index"),
    path('signup', ChessPlayerSignup.as_view(), name="signup"),
    path('dashboard', user_required(ChessPlayerDashboard.as_view()), name="dashboard")
]