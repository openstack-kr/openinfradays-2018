from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from modeltranslation.admin import TranslationAdmin

from .models import Program, Speaker, ProgramCategory, ProgramDate, \
    ProgramTime, Room


class ProgramAdmin(SummernoteModelAdmin, TranslationAdmin):
    list_display = ('id', 'name', )
    list_editable = ('name', )
    ordering = ('id', )
    search_fields = ('name', )
admin.site.register(Program, ProgramAdmin)


class SpeakerAdmin(SummernoteModelAdmin, TranslationAdmin):
    list_display = ('id', 'name', 'email', 'organization')
    list_editable = ('name', 'organization')
    ordering = ('id', )
    search_fields = ('name', 'email')
admin.site.register(Speaker, SpeakerAdmin)


class ProgramCategoryAdmin(SummernoteModelAdmin, TranslationAdmin):
    list_display = ('id', 'name', 'slug', )
    list_editable = ('name', 'slug', )
    ordering = ('id', )
    search_fields = ('name', )
admin.site.register(ProgramCategory, ProgramCategoryAdmin)


class ProgramDateAdmin(SummernoteModelAdmin, TranslationAdmin):
    list_display = ('id', 'day', )
    list_editable = ('day', )
    ordering = ('day', )
admin.site.register(ProgramDate, ProgramDateAdmin)


class RoomAdmin(SummernoteModelAdmin, TranslationAdmin):
    list_display = ('id', 'name', )
    list_editable = ('name', )
    ordering = ('id', )
admin.site.register(Room, RoomAdmin)


class ProgramTimeAdmin(SummernoteModelAdmin, TranslationAdmin):
    list_display = ('id', 'name', 'begin', 'end', 'day')
    list_editable = ('name', 'begin', 'end', 'day')
    ordering = ('id', )
admin.site.register(ProgramTime, ProgramTimeAdmin)
