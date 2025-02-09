from django.urls import path
from .views import ServiceListView, PortfolioListView, TeamListView, VideoListView

urlpatterns = [
    path("services/", ServiceListView.as_view(), name="services-list"),
    path("portfolio/", PortfolioListView.as_view(), name="portfolio-list"),
    path("team/", TeamListView.as_view(), name="team-list"),
    path("video/", VideoListView.as_view(), name="video-list"),


]
