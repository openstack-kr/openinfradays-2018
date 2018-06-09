from django.db import models
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.widgets import SummernoteWidget
from modeltranslation.admin import TranslationAdmin

from .models import Program, Speaker, ProgramCategory, ProgramDate, \
    ProgramTime, Room, Sponsor, SponsorLevel


class SummernoteWidgetWithCustomToolbar(SummernoteWidget):
    def template_contexts(self):
        contexts = super(SummernoteWidgetWithCustomToolbar, self).template_contexts()
        contexts['width'] = '960px'
        return contexts


class SponsorAdmin(SummernoteModelAdmin, TranslationAdmin):
    formfield_overrides = {models.TextField: {'widget': SummernoteWidgetWithCustomToolbar}}
    list_display = ('id', 'name', 'slug', )
    ordering = ('name',)
    list_editable = ('name', 'slug',)
    search_fields = ('name', 'slug',)
admin.site.register(Sponsor, SponsorAdmin)


class SponsorLevelAdmin(SummernoteModelAdmin, TranslationAdmin):
    list_display = ('id', 'order', 'name',)
    list_editable = ('order', 'name',)
    ordering = ('order',)
    search_fields = ('name',)
admin.site.register(SponsorLevel, SponsorLevelAdmin)


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


class SummernoteWidgetWithCustomToolbar(SummernoteWidget):
    def template_contexts(self):
        contexts = super(SummernoteWidgetWithCustomToolbar, self)\
            .template_contexts()
        contexts['width'] = '960px'
        return contexts


class FlatPageAdmin(TranslationAdmin):
    formfield_overrides = {
        models.TextField: {'widget': SummernoteWidgetWithCustomToolbar}}

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
