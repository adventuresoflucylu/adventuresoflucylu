from django import 							forms
from django.forms import 					ModelForm
from django.contrib.auth.models import	User

from users.models import 					Page, Category, BookUser, UserProfile


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = "__all__"

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        
        # If url is not empty and doesn't start with 'http://' add 'http://' to the beginning
        if url and not url.startswith('http://'):
            url = 'http://' + url
            
            cleaned_data['url'] = url
        return cleaned_data

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign keys
        fields = ('title', 'url','views')

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
#		fields = ('doggiesname')
#		fields = ('username', 'email')
		fields = ('website', 'doggiesname', 'picture')

class RegistrationForm(ModelForm):
	username		= forms.CharField(label=(u'User Name'))
	email			= forms.EmailField(label=(u'Email Address'))
	password		= forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
	password1	= forms.CharField(label=(u' Verify Password'), widget=forms.PasswordInput(render_value=False))

	class Meta:
		model = BookUser
		fields = ('username', 'email', 'password')
#		exclude = ('user',)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError("That Username is already taken, please select another.")

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError("That Email is already taken, please select another.")

	def clean(self):
		cleaned_data = super(RegistrationForm, self).clean()
		password = cleaned_data['password']
		password1 = cleaned_data['password1']
		if password and password1 and password == password1:
			pass
		else:
			raise forms.ValidationError('The passwords did not match, Please try again.')
		return cleaned_data

#	def clean_password(self):
#		password = self.cleaned_data['password']
#		password1 = self.cleaned_data['password1']
#		if password != password1:
#			raise forms.ValidataionError("The password did not match. Please try again.")
#		return password

class LoginForm(forms.Form):
	username	= forms.CharField(label=(u'User Name'))
	password	= forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))

