from importlib.resources import path
from random import lognormvariate
from django.contrib import admin
from .models import Ticket, Review
# Register your models here.

admin.site.register(Ticket)

