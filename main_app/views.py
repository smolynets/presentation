from django.shortcuts import render
from . models import Frame, PageOfSlider, PresentasionName, SubheaderText, SubheaderImage


def index(request):
	frames = Frame.objects.all()
	slides = PageOfSlider.objects.all()
	presentation_name = PresentasionName.objects.get()
	subheader_text = SubheaderText.objects.all().first()
	subheader_image = SubheaderImage.objects.all().first()
	return render(request, 'index.html', {"frames": frames,
										  "slides": slides,
										  "presentation_name": presentation_name,
										  "subheader_text": subheader_text,
										  "subheader_image": subheader_image})
