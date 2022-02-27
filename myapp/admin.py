from django.contrib import admin

# Register your models here.
from .models import House, NewCustomer, HelpDesk

admin.site.register(House)
# admin.site.register(RegisteredCustomer)
admin.site.register(NewCustomer)
admin.site.register(HelpDesk)