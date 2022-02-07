from django.urls import path

from .views import (
                    HomePageView,
                    TicketDetailView,
                    ReviewDetailView,
                    TicketCreateView,
                    ReviewCreateView,
                    TicketUpdateView,
                    ReviewUpdateView,
                    TicketDeleteView,
                    ReviewDeleteView,
                    Posts,
                    Flux,
                    Subscribers
                    )   
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("ticket/<int:pk>/", TicketDetailView.as_view(), name="ticket-detail"),
    path("review/<int:pk>/", ReviewDetailView.as_view(), name="review-detail"),
    path("ticket/new/", TicketCreateView.as_view(), name="ticket-create"),
    path("review/new/", ReviewCreateView.as_view(), name="review-create"),
    path("ticket/<int:pk>/update/", TicketUpdateView.as_view(), name="ticket-update"),
    path("review/<int:pk>/update/", ReviewUpdateView.as_view(), name="review-update"),
    path("ticket/<int:pk>/delete/", TicketDeleteView.as_view(), name="ticket-delete"),
    path("review/<int:pk>/delete/", ReviewDeleteView.as_view(), name="review-delete"),
    path("posts/", Posts.as_view(), name="posts-users"),
    path("subscribers/", Subscribers.as_view(), name="subscribers"),
    path("", Flux.as_view(), name="flux"),
]
