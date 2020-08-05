from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Contact

# Register your models here.
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Extra User Information',
            {
                'fields': (
                    'resume',
                    
                    
                ),
            },
        ),

    )
    

admin.site.register(User,CustomUserAdmin)
admin.site.register(Contact)