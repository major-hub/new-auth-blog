from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_img')
    fields = ('user', ('img', 'get_img'))
    readonly_fields = ('get_img', )

    def get_img(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" width="100px">')

    get_img.short_description = 'Hozirgi rasm'
