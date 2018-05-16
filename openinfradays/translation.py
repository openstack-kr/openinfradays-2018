from modeltranslation.translator import translator, TranslationOptions
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

