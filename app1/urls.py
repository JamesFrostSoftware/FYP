from django.urls import path
from .views import MovieListView, MovieDetailView, MovieCreateView, MovieCompare, SuggestionView
from . import views

urlpatterns = [
    path('', MovieListView.as_view(), name='app1-home'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movie/new/', MovieCreateView.as_view(), name='movie-create'),
    path('getASuggestion/', views.getASuggestion, name='app1-getASuggestion'),
    path('Get-A-Suggestion/', SuggestionView.as_view(), name='app1-getASuggestion2'),
]