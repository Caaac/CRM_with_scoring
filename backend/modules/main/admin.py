from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from modules.main.models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('login', 'email', 'name', 'last_name', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    
    fieldsets = (
        (None, {'fields': ('login', 'password')}),
        ('Персональная информация', {'fields': ('name', 'last_name', 'email', 'personal_gender', 'personal_photo')}),
        # ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Даты', {'fields': ('last_login', 'date_register')}),
         ('Права доступа', {
          'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        
    )
      
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('login', 'email', 'password1', 'password2'),
        }),
    )
    
    filter_horizontal = ('groups', 'user_permissions')
    
    search_fields = ('login', 'email')
    ordering = ('login',)
    readonly_fields = ('date_register',)
    
    # # Убираем filter_horizontal для несуществующих полей
    # filter_horizontal = ()  # Удаляем ('groups', 'user_permissions')
    
     # Помечаем нередактируемые поля как read-only
    readonly_fields = ('last_login', 'date_register')  # Добавляем last_login сюда

admin.site.register(User, CustomUserAdmin)