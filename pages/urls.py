from django.urls import path

from .views import (
                    HomePageView,
                    TicketDetailView,
                    ReviewDetailView,
                    TicketCreateView,
                    ReviewCreateView,
                    Flux,
                    Subscribers
                    )   
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("ticket/<int:pk>/", TicketDetailView.as_view(), name="ticket-detail"),
    path("review/<int:pk>/", ReviewDetailView.as_view(), name="review-detail"),
    path("ticket/new/", TicketCreateView.as_view(), name="ticket-create"),
    path("review/new/", ReviewCreateView.as_view(), name="review-create"),
    path("subscribers/", Subscribers.as_view(), name="subscribers"),
    path("", Flux.as_view(), name="flux"),
]
