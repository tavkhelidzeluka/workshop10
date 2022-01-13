from django.contrib import admin

from users.models import User

# Register your models here.

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    readonly_fields = ['password', 'date_joined', 'last_login']