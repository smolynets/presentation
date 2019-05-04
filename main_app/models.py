from django.db import models


class Frame(models.Model):
	name = models.CharField(max_length=20)
	text = models.TextField(blank=False)

	class Meta:
		verbose_name = 'Frame'
		verbose_name_plural = 'Frames'

	def __str__(self):
		return self.name
