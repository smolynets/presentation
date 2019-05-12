from django.contrib import admin
from .models import Frame, PageOfSlider
from django_summernote.admin import SummernoteModelAdmin

class Sumernote(SummernoteModelAdmin):
	summernote_fields = ('text',)

admin.site.register(Frame, Sumernote)
admin.site.register(PageOfSlider, Sumernote)
