from multiprocessing import get_context
from django.views.generic import (
                                TemplateView,
                                ListView,
                                DetailView,
                                CreateView
                                )

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from pages.models import Ticket, Review



posts = [
    {
        "author": "Mathieu",
        "title": "Critique",
        "rating": "4",
        "content": "Exceptionnel",
        "date_posted": "24 janvier 2022",
    },
    {
        "author": "User 1",
        "title": "Ticket",
        "content": "Demande une critique",
        "image": "Lien image",
        "date_posted": "25 janvier 2022",
    },
]


@method_decorator(login_required, name="dispatch")
class HomePageView(TemplateView):
    template_name = "home.html"
    # Not working atm
    ordering = ["-time_created"]
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tickets"] = Ticket.objects.all()
        context["reviews"] = Review.objects.all().select_related("ticket")
        return context


class TicketDetailView(DetailView):
    model = Ticket
    template_name = "ticket_detail.html"


class ReviewDetailView(DetailView):
    model = Review
    template_name = "review_detail.html"


class TicketCreateView(CreateView):
    model = Ticket
    fields = ["title", "description", "image"]
    template_name = "ticket_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ReviewCreateView(CreateView):
    model = Review
    fields = ["rating", "headline", "body"]
    template_name = "review_form.html"


class Flux(ListView):
    pass


class Subscribers(TemplateView):
    template_name = "subscribers.html"
