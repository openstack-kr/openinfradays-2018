from modeltranslation.translator import translator, TranslationOptions
from django.contrib.flatpages.models import FlatPage
from .models import Program, Speaker, ProgramCategory, ProgramDate, \
    ProgramTime, Room


class ProgramTranslationOptions(TranslationOptions):
    fields = ('name', )
translator.register(Program, ProgramTranslationOptions)


class SpeakerTranslationOptions(TranslationOptions):
    fields = ('desc', )
translator.register(Speaker, SpeakerTranslationOptions)


class ProgramCategoryTranslationOptions(TranslationOptions):
    fields = ('name', )
translator.register(ProgramCategory, ProgramCategoryTranslationOptions)


class ProgramDateTranslationOptions(TranslationOptions):
    fields = ()
translator.register(ProgramDate, ProgramDateTranslationOptions)


class ProgramTimeTranslationOptions(TranslationOptions):
    fields = ()
translator.register(ProgramTime, ProgramTimeTranslationOptions)


class RoomTranslationOptions(TranslationOptions):
    fields = ()
translator.register(Room, RoomTranslationOptions)


class FlatPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)
translator.register(FlatPage, FlatPageTranslationOptions)
