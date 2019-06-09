from django.shortcuts import render
from . models import Frame, PageOfSlider, PresentasionName


def index(request):
	frames = Frame.objects.all()
	slides = PageOfSlider.objects.all()
	presentation_name = PresentasionName.objects.get()
	return render(request, 'index.html', {"frames": frames,
										  "slides": slides,
										  "presentation_name": presentation_name})
