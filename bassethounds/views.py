import datetime

from django.http							import 	HttpResponseRedirect, HttpResponse
from django.shortcuts					import	render_to_response, render
from django.template						import	RequestContext
from django.contrib.auth				import	authenticate, login, logout
from django.contrib.auth.models		import 	User
from django.contrib.auth.decorators import	login_required

#from users.models import Books
from users.models import 				Category, Page
from users.views import					get_profile, get_category_list, mytime

def bassethounds(request):
	context_dict = get_profile(request)
	return render_to_response('bassethounds.html', context_dict, context_instance=RequestContext(request))

def thebreed(request):
	context_dict = get_profile(request)
	return render_to_response('thebreed.html', context_dict, context_instance=RequestContext(request)) 

def rescues(request):
	context_dict = get_profile(request)
	return render_to_response('rescues.html', context_dict, context_instance=RequestContext(request)) 

def holder(request):
	context_dict = get_profile(request)
	return render_to_response('holder.html', context_dict, context_instance=RequestContext(request)) 

# Create your views here.
