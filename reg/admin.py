from django.contrib import admin
from .models import hspinfo, usrinfo, User

# Register your models here.
admin.site.register(User)

@admin.register(usrinfo)
class UserDisp(admin.ModelAdmin):
    list_display = ('id', 'full_Name', 'city', 'address', 'phone', 'email')

@admin.register(hspinfo)
class Hospital(admin.ModelAdmin):
    list_display = ('id', 'hospital_Name', 'city', 'address', 'phone', 'email', 'no_of_beds', 'no_of_ventilators', 'no_of_vaccines')#'username')
