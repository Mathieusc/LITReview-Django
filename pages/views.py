from multiprocessing import get_context
from django.views.generic import (
                                TemplateView,
                                ListView,
                                DetailView,
                                CreateView,
                                UpdateView,
                                DeleteView
                                )

from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from pages.models import Ticket, Review


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


# Details models
class TicketDetailView(DetailView):
    model = Ticket
    template_name = "ticket_detail.html"


class ReviewDetailView(DetailView):
    model = Review
    template_name = "review_detail.html"


# Create models
class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    fields = ["title", "description", "image"]
    template_name = "ticket_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ReviewCreateView(CreateView):
    model = Review
    fields = ["headline", "rating", "body"]
    template_name = "review_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Update models
class TicketUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ticket
    fields = ["title", "description", "image"]
    template_name = "ticket_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ticket = self.get_object()
        if self.request.user == ticket.user:
            return True
        return False


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = [ "headline", "rating", "body"]
    template_name = "ticket_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.user:
            return True
        return False


# Delete models
class TicketDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ticket
    template_name = "ticket_confirm_delete.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ticket = self.get_object()
        if self.request.user == ticket.user:
            return True
        return False


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = "review_confirm_delete.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.user:
            return True
        return False


class Posts(TemplateView):
    template_name = "posts.html"
    # Not working atm
    ordering = ["-time_created"]
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tickets"] = Ticket.objects.all()
        context["reviews"] = Review.objects.all().select_related("ticket")
        return context


class Flux(ListView):
    pass


class Subscribers(TemplateView):
    template_name = "subscribers.html"
