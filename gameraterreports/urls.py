from django.urls import path

from gameraterreports.views.base import BaseList

from .views import Top5GameList, Bottom5GameList, CategoryGameCountList
from .views import GamesGreaterThan5PlayersList
from .views import MostReviewedGameList
from .views import GamerMostGamesAddedList
from .views import GamerMostReviewsList
from .views import GamesUnderAge8List
from .views import GamesNoPicsList

urlpatterns = [
    path('reports/top5games', Top5GameList.as_view()),
    path('reports/bottom5games', Bottom5GameList.as_view()),
    path('reports/categoryGameCounts', CategoryGameCountList.as_view()),
    path('reports/gamesForMoreThan5', GamesGreaterThan5PlayersList.as_view()),
    path('reports/mostReviewedGame', MostReviewedGameList.as_view()),
    path('reports/gamesUnderAge8', GamesUnderAge8List.as_view()),
    path('reports/gamesNoPics', GamesNoPicsList.as_view()),
    path('reports/gamerMostGamesAdded', GamerMostGamesAddedList.as_view()),
    path('reports/gamerMostReviews', GamerMostReviewsList.as_view()),
    path('reports/base', BaseList.as_view()),
]
