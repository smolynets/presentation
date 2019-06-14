from django.db import models
from solo.models import SingletonModel


class Frame(models.Model):
	name = models.CharField(max_length=20)
	text = models.TextField(blank=True)
	is_slider = models.BooleanField(default=False)

	class Meta:
		verbose_name = 'Frame'
		verbose_name_plural = 'Frames'

	def __str__(self):
		return self.name


class PageOfSlider(models.Model):
	name = models.CharField(max_length=20)
	text = models.TextField(blank=False)

	class Meta:
		verbose_name = 'PageOfSlider'
		verbose_name_plural = 'PageOfSliders'

	def __str__(self):
		return self.name


class PresentasionName(SingletonModel):
    name = models.CharField(max_length=255, default='Presentasion Name')

    def __str__(self):
        return u"PresentasionName"

    class Meta:
        verbose_name = "PresentasionName"


class SubheaderText(SingletonModel):
    headline = models.CharField(max_length=255, default='Subheader_text name')
    text = models.TextField()

    class Meta:
        verbose_name = 'SubheaderText'
        verbose_name_plural = 'SubheaderTexts'
    
    def __str__(self):
        return self.headline
