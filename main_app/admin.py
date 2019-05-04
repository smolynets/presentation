from django.contrib import admin
from .models import Frame
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
	summernote_fields = ('text',)

admin.site.register(Frame, PostAdmin)
