from django.contrib import admin

from .models import TourRequest
from users.models import Client, Manager


admin.site.register(Client)
admin.site.register(Manager)
admin.site.register(TourRequest)


