from django.shortcuts import render
from . models import Frame


def index(request):
	frames = Frame.objects.all()
	return render(request, 'index.html', {"frames": frames})
