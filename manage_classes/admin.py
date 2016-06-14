from django.contrib import admin
from .models import Classes
from .models import Sections
# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Sections
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]



admin.site.register(Classes,QuestionAdmin)
admin.site.register(Sections)
