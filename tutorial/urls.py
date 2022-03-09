from django.urls import path
from .views import TutorialListView, TutorialDetailView, SearchView

urlpatterns = [
    path('', TutorialListView.as_view(), name="tutorial_list"),
    path('<slug:slug>', TutorialDetailView.as_view(), name="tutorial_detail"),
    path('search/', SearchView.as_view(), name="search"),
]