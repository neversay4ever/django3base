from django.contrib import admin

# Register your models here.
from .models import Data


class DataAdmin(admin.ModelAdmin):
    model = Data
    list_display = [
        field.name for field in Data._meta.get_fields() if field.name != 'id']


admin.site.register(Data, DataAdmin)
