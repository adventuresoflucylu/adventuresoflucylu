from django.shortcuts import render_to_response
from django.template import RequestContext
#from books.models import Bassethounds

def bholder(request):
	return render_to_response('bholder.html', {}) 

def holder(request):
	return render_to_response('holder.html', {}) 

def thebreed(request):
	return render_to_response('holder.html', {}) 

#def TheBigJob(request):
#	:

def rescues(request):
	return render_to_response('holder.html',{}) 

# Create your views here.
