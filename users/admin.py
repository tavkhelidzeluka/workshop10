from django.contrib import admin

from users.models import User

# Register your models here.

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    readonly_fields = ['date_joined', 'password', 'last_login']