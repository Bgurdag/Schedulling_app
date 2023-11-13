from django.contrib import admin

# Register models .
from .models import Event

admin.site.register(Event)