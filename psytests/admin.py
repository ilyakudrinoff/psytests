from django.contrib import admin

from .models import Psyhologes, Tests, Results


@admin.register(Psyhologes)
class PsyhologesAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'gender', 'old', 'instagram', 'telegram', 'email',)
    list_editable = ('email',)
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at', 'old',)
    empty_value_display = '-пусто-'


@admin.register(Tests)
class TestsAdmin(admin.ModelAdmin):
    list_display = ('name', 'question', 'answer', 'adult',)
    list_editable = ('question',)
    search_fields = ('question', 'answer', 'name',)
    list_filter = ('name', 'adult',)
    empty_value_display = '-пусто-'


@admin.register(Results)
class ResultsAdmin(admin.ModelAdmin):
    list_display = ('psyholog', 'test', 'question', 'answer',)
    search_fields = ('psyholog', 'test', 'question',)
    list_filter = ('psyholog', 'test',)
    empty_value_display = '-пусто-'
