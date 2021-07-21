from django.contrib import admin

# Register your models here.
from .models import Clients

class ClientsAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email',)

admin.site.register(Clients, ClientsAdmin)
