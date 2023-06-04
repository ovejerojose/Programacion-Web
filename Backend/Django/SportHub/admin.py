from django.contrib import admin
from SportHub.models import Productos,CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.


admin.site.register(Productos)
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass
