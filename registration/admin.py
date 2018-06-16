import string
import random

from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist

from .models import InviteCode, Registration


# Register your models here.
def id_generator():
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(6))


class InviteCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'registered', 'user',)
    list_editable = ()
    ordering = ('code',)
    search_field = ('code',)

    def get_form(self, request, obj=None, **kwargs):
        form = super(InviteCodeAdmin, self).get_form(request, obj, **kwargs)
        duplicated = True
        code = id_generator()
        while duplicated:
            try:
                InviteCode.objects.get(code=code)
                code = id_generator()
            except ObjectDoesNotExist:
                duplicated = False
        form.base_fields['code'].initial = code
        return form


admin.site.register(InviteCode, InviteCodeAdmin)


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'invite_code',)
    list_editable = ()
    readonly_fields = ('confirmed', )
    ordering = ('name',)
    search_fields = ('name', 'email', 'invite_code',)


admin.site.register(Registration, RegistrationAdmin)
