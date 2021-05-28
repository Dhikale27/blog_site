from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomeUserCreationForm, CustomeUserChangeForm
from .models import CustomUser

# Register your models here.


class CustomeUserAdmin(UserAdmin):
    add_form = CustomeUserCreationForm
    form = CustomeUserChangeForm
    model = CustomUser

    list_display = ['email', 'username', 'age', 'is_staff', ]
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('age',)}),)

    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('age',)}),
                                               )


admin.site.register(CustomUser, CustomeUserAdmin)
