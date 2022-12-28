from django.contrib import admin
from Myapp.models import AddDonarModle

@admin.register(AddDonarModle)
class AddDonarModleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'blood_group', 'age','email', 'phone']
    #ordering = ('name')
    search_fields = ('name', 'blood_group', 'address')
