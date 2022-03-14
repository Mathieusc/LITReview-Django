from django.db import models
from django.conf import settings
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-time_created"]

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("ticket-detail", kwargs={"pk": self.pk})


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE, null=True, blank=True, related_name="review_from")
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-time_created"]

    def __str__(self):
        return str(self.headline)

    def get_absolute_url(self):
        return reverse("review-detail", kwargs={"pk": self.pk})
