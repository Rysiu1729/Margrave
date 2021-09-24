from django.contrib import admin

# Register your models here.

from django.db import models
from django.forms import TextInput, Textarea

from game.models import Chapter
from game.models import Section
from game.models import Page
from game.models import Option
from game.models import Effect
from game.models import Person




class Options(admin.TabularInline):
    model = Option
    show_change_link = True


class PageAdmin(admin.ModelAdmin):
    inlines = [
        Options
    ]
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 40, 'cols': 100})},
    }


class Pages(admin.TabularInline):
    model = Page
    show_change_link = True


class SectionsAdmin(admin.ModelAdmin):
    inlines = [
        Pages
    ]

class Sections(admin.TabularInline):
    model = Section
    show_change_link = True

class ChapterAdmin(admin.ModelAdmin):
    inlines = [
        Sections
    ]

admin.site.register(Chapter,ChapterAdmin)
admin.site.register(Section,SectionsAdmin)
admin.site.register(Page,PageAdmin)
admin.site.register(Option)
admin.site.register(Effect)
admin.site.register(Person)

