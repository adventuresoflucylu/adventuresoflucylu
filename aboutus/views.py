from django.shortcuts import render_to_response
from django.template import RequestContext
from books.models import Book

def bholder(request):
	return render_to_response('bholder.html', {}) 

def thebigjob(request):
	return render_to_response('thebigjob.html', {}) 

#def TheBigJob(request):
#	:

def booboobear(request):
	return render_to_response('booboobear.html',{}) 

def tbd(request):
	return render_to_response('tbd.html',{}) 

# Create your views here.
