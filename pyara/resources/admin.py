from django.contrib import admin

from .models import User
from .models import Answer
from .models import Question

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title','date')
    list_filter = ('title','date')
    prepopulated_fields = {'slug':('title',)}

# Register your models here.
admin.site.register(User)
admin.site.register(Answer)
admin.site.register(Question, ResourceAdmin)
