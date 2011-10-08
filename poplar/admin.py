
from django.contrib import admin
from poplar.models import *

class GroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Person)
admin.site.register(Note)
admin.site.register(Group, GroupAdmin)
