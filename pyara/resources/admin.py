from django.contrib import admin

from .models import Answer
from .models import Question
from .models import Quote


class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_filter = ('title', 'date')
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Quote)
admin.site.register(Answer)
admin.site.register(Question, ResourceAdmin)
