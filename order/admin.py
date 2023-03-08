from django.contrib import admin

# Register your models here.
from order.models import Orders

admin.site.register(Orders)