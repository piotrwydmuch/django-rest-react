from django.contrib import admin

from .models import Advertisement
from .models import Company

admin.site.register(Advertisement)
admin.site.register(Company)
