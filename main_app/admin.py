from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from solo.admin import SingletonModelAdmin

from .models import Frame, PageOfSlider, PresentasionName, SubheaderText, SubheaderImage


class Sumernote(SummernoteModelAdmin):
	summernote_fields = ('text',)

admin.site.register(Frame, Sumernote)
admin.site.register(PageOfSlider, Sumernote)
admin.site.register(SubheaderText, Sumernote)
admin.site.register(PresentasionName, SingletonModelAdmin)
admin.site.register(SubheaderImage, SingletonModelAdmin)
