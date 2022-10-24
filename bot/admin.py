from django.contrib import admin

from .models import Item, ItemsSet, Person

admin.site.register(Item)
admin.site.register(ItemsSet)
admin.site.register(Person)
# Register your models here.
