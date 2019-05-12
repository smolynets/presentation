from django.shortcuts import render
from . models import Frame, PageOfSlider


def index(request):
	frames = Frame.objects.all()
	slides = PageOfSlider.objects.all()
	return render(request, 'index.html', {"frames": frames,
										  "slides": slides})
