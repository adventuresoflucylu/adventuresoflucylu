import datetime
from django.http							import 	HttpResponseRedirect, HttpResponse
from django.shortcuts					import	render_to_response, render
from django.template						import	RequestContext
from django.contrib.auth				import	authenticate, login, logout
from django.contrib.auth.models		import 	User
from django.contrib.auth.decorators import	login_required

from users.views import					get_profile, get_category_list, mytime

def index(request):
	context_dict = get_profile(request)
#	context_dict['base_html'] = "none.html"
	return render_to_response('index.html', context_dict, context_instance=RequestContext(request)) 

def home(request):
	context_dict = get_profile(request)
#	context_dict['base_html'] = "none.html"
	return render_to_response('home.html', context_dict, context_instance=RequestContext(request))


