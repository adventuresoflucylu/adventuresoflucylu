import datetime

from django.http							import 	HttpResponseRedirect, HttpResponse
from django.shortcuts					import	render_to_response, render
from django.template						import	RequestContext
from django.contrib.auth				import	authenticate, login, logout
from django.contrib.auth.models		import 	User
from django.contrib.auth.decorators import	login_required

#from books.models import 				Books, TheBigJob
from books.models import 				AllBooks, TheBigJob
from users.models import 				Category, Page
from users.views import					get_profile, get_category_list, mytime

def books(request):
	context_dict = get_profile(request)
	return render_to_response('books.html', context_dict, context_instance=RequestContext(request)) 

def thebigjob(request):
#	base_html = "advbase.html"
	context_dict = get_profile(request)
#	context_dict['base_html'] = "advbase.html"
	return render_to_response('thebigjob.html', context_dict, context_instance=RequestContext(request)) 

def goingtoohio(request):
	context_dict = get_profile(request)
	return render_to_response('goingtoohio.html', context_dict, context_instance=RequestContext(request)) 

def booboobear(request):
	context_dict = get_profile(request)
	return render_to_response('booboobear.html', context_dict, context_instance=RequestContext(request)) 

def tbd(request):
	context_dict = get_profile(request)
	return render_to_response('tbd.html', context_dict, context_instance=RequestContext(request)) 
