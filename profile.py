import datetime

from django.http							import 	HttpResponseRedirect, HttpResponse
from django.shortcuts					import	render_to_response, render
from django.template						import	RequestContext
from django.contrib.auth				import	authenticate, login, logout
from django.contrib.auth.models		import 	User
from django.contrib.auth.decorators import	login_required

#from books.models import Books
from users.models import 				Category, Page
from users.views import					get_category_list

def get_profile2(request):
	if request.user.is_authenticated():
    	# Do something for authenticated users.
		myusername = request.user.username
		return "%s, You are logged in." % myusername
	else:
    	# Do something if user is not authenticated .
		Me = request.user.username
		return " ::%s, You are Not logged in." % Me

def get_profile(request):
	if request.user.is_authenticated():
    # Do something for authenticated users.
		context = RequestContext(request)
		cat_list = get_category_list()
		context_dict = {'cat_list': cat_list}
		currentU = User.objects.get(username=request.user)
  	 
		try:
			up = UserProfile.objects.get(user=currentU)
		except:
			up = None
   
		context_dict['user'] = currentU
		context_dict['userprofile'] = up
		return context_dict
	else:
		pass
#		return render_to_response('aboutus.html', context_instance=RequestContext(request))
#		return render('aboutus.html', request)
    

def mytime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)

