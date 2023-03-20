from django.contrib import admin
from .models import Question, Choice, Anfrage

#choices to be displayed along with questions
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information',{'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
class AnfrageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Date information', {'fields': ['bestellzeit'], 'classes': ['collapse']}),
    ]


# Register your models here.
admin.site.register(Anfrage)
#admin.site.register(Choice)

