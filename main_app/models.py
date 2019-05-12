from django.db import models


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
