from django.shortcuts import render
from . models import Frame, PageOfSlider, PresentasionName, SubheaderText, CopyRight


def index(request):
	frames = Frame.objects.all()
	slides = PageOfSlider.objects.all()
	presentation_name = PresentasionName.objects.get()
	subheader_text = SubheaderText.objects.all().first()
	copy_right = CopyRight.objects.get()
	return render(request, 'index.html', {"frames": frames,
										  "slides": slides,
										  "presentation_name": presentation_name,
										  "subheader_text": subheader_text,
										  "copy_right": copy_right})
