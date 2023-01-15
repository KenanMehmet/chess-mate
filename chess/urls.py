from django.urls import path

from .views import ChessIndex

urlpatterns = [
    path('', ChessIndex.as_view(), name="index"),
]