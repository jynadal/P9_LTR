from django.contrib import admin

# Register your models here.
from Review.models import Review, Ticket

admin.site.register(Review)
admin.site.register(Ticket)