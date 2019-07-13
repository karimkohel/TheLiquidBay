from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.

admin.site.site_header = 'TheLiquidBay'

admin.site.unregister(Group)
