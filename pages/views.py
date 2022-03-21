from itertools import chain
from django.shortcuts import render
from django.db.models import Value, Q
from django.db.models.fields import CharField
from django.shortcuts import redirect
from django.views.generic import (
    TemplateView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from accounts.models import CustomUser, UserFollows
from pages.models import Ticket, Review
from .forms import ReviewForm


@login_required
def home_page_view(request):
    tickets = get_users_viewable_tickets(request.user)
    tickets = tickets.annotate(content_type=Value("TICKET", CharField()))

    reviews = get_users_viewable_reviews(request.user)
    reviews = reviews.annotate(content_type=Value("REVIEW", CharField()))

    posts = sorted(
        chain(reviews, tickets), key=lambda post: post.time_created, reverse=True
    )

    context = {
        "posts": posts,
    }

    return render(request, "home.html", context)


def get_users_viewable_tickets(user):
    users = UserFollows.objects.filter(user=user)
    user_follow = CustomUser.objects.filter(followed_by__in=users)

    tickets = Ticket.objects.filter(Q(user__in=user_follow) | Q(user=user))

    return tickets


def get_users_viewable_reviews(user):
    users = UserFollows.objects.filter(user=user)
    user_follow = CustomUser.objects.filter(followed_by__in=users)

    reviews = Review.objects.filter(
        Q(user__in=user_follow)
        | Q(ticket__user=user)
        | Q(ticket__user__in=user_follow)
        | Q(user=user)
    )

    return reviews


# Details models
class TicketDetailView(DetailView):
    model = Ticket
    template_name = "tickets/ticket_detail.html"


class ReviewDetailView(DetailView):
    model = Review
    template_name = "reviews/review_detail.html"


# Create models
class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    fields = ["title", "description", "image"]
    template_name = "tickets/ticket_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReviewCreateView(CreateView):
    model = Review
    fields = ["headline", "rating", "body"]
    template_name = "reviews/review_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def review_response(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    # ticket = get_object_or_404(Ticket, pk=ticket_id)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES, instance=ticket)

        if review_form.is_valid():
            review = Review()
            review.user = request.user
            review.rating = review_form.cleaned_data["rating"]
            review.headline = review_form.cleaned_data["headline"]
            review.body = review_form.cleaned_data["body"]
            review.ticket = ticket
            review.save()
            return redirect("home")
    else:
        review_form = ReviewForm()

    context = {"review_form": review_form, "ticket": ticket}

    return render(request, "tickets/ticket_response.html", context)


# Update models
class TicketUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ticket
    fields = ["title", "description", "image"]
    template_name = "tickets/ticket_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ticket = self.get_object()
        if self.request.user == ticket.user:
            return True
        return False


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ["headline", "rating", "body"]
    template_name = "reviews/review_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.user:
            return True
        return False


# Delete models
class TicketDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ticket
    template_name = "tickets/ticket_confirm_delete.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ticket = self.get_object()
        if self.request.user == ticket.user:
            return True
        return False


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = "reviews/review_confirm_delete.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.user:
            return True
        return False


class Posts(TemplateView):
    template_name = "users/posts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tickets"] = Ticket.objects.all()
        context["reviews"] = Review.objects.all().select_related("ticket")
        return context


class Flux(TemplateView):
    template_name = "users/flux.html"


@login_required
def subscribers(request):
    followed_by = UserFollows.objects.filter(user=request.user)
    following = UserFollows.objects.filter(followed_user=request.user)

    if request.method == "POST":
        follow_user = request.POST.get("follow_user")
        if follow_user == request.user.username:
            messages.error(request, "Vous ne pouvez pas vous suivre.")
            return redirect("subscribers")

        existing_user = CustomUser.objects.filter(username=follow_user)

        if existing_user:
            existing_user = CustomUser.objects.get(username=follow_user)
            try:
                user_follows = UserFollows(
                    user=request.user, followed_user=existing_user
                )
                user_follows.save()
                messages.info(request, f"Vous suivez {existing_user.username}")
            except:
                messages.info(request, f"Vous suivez déjà cet utilisateur.")
                return redirect("subscribers")
        else:
            messages.error(request, "Cet utilisateur est introuvable.")
            return redirect("subscribers")

    context = {"followed_by": followed_by, "following": following}

    return render(request, "users/subscribers.html", context)


@login_required
def unsubscribe(request, followed_by_id, following_id):
    followed_by = UserFollows.objects.filter(
        user_id=following_id, followed_user_id=followed_by_id
    )
    if followed_by:
        followed_by = UserFollows.objects.get(
            user_id=following_id, followed_user_id=followed_by_id
        )
        followed_by.delete()
    return redirect("subscribers")
