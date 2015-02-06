from django.http 							import HttpResponseRedirect, HttpResponse 
from django.template 					import RequestContext
from django.shortcuts 					import render_to_response, render
from django.contrib.auth 				import authenticate, login, logout
from django.contrib.auth.models		import User
from django.core.context_processors	import csrf
from django.contrib.auth.decorators	import login_required

from users.models 						import BookUser, UserProfile, Category, Page
from users.forms 							import RegistrationForm, LoginForm, UserForm, UserProfileForm

import datetime

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

def get_category_list(max_results=0, starts_with=''):
    cat_list = []
    if starts_with:
        cat_list = Category.objects.filter(name__startswith=starts_with)
    else:
        cat_list = Category.objects.all()

    if max_results > 0:
        if (len(cat_list) > max_results):
            cat_list = cat_list[:max_results]

    for cat in cat_list:
        cat.url = encode_url(cat.name)
    
    return cat_list


def LoginRequest(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/profile/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'login.html', {})


def LoginRequest2(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/profile/')
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			name 		= form.cleaned_data['name']
			password = form.cleaned_data['password']
			users = authenticate(username=ame, password=password)
			if users is not None:
				login(request, users)
				return HttpResponseRedirect('/profile/')
			else:
#				return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
				return render_to_response('account/login.html', {'form': form}, context_instance=RequestContext(request))
#				return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
	else:
		''' User is not submitting the form, show the login form '''
		form = LoginForm()
		context = {'form': form}
		context = {'form': form}
#		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		return render_to_response('account/login.html', {'form': form}, context_instance=RequestContext(request))
#		return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))

def RegisterBookUser(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'rango/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

@login_required
def Profile(request):
	context = RequestContext(request)
	cat_list = get_category_list()
	context_dict = {'cat_list': cat_list}
	u = User.objects.get(username=request.user)
    
	try:
		up = UserProfile.objects.get(user=u)
	except:
		up = None
    
	context_dict['user'] = u
	context_dict['userprofile'] = up
	return render_to_response('profile.html', context_dict, context)

@login_required
def Profile3(request):
	if request.method == 'POST':
		form = UserProfileForm(request.POST, instance=request.user.profile)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/loggedin')
		else:
			user = request.user
			profile = user.profile
			form = UserProfileForm(instance=profile)
        
	args = {}
	args.update(csrf(request))
    
	args['form'] = form
    
	return render_to_response('profile.html', args)   



@login_required
def Profile2(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login/')
#	users = request.user.get_profile()
	users = request.user.profile
	context = {'users': users}
	return render_to_response('profile.html', context, context_instance=RequestContext(request))

def LogoutRequest(request):
	logout(request)
	return HttpResponseRedirect('/')
