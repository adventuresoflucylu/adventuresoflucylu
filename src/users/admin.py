from django.contrib import admin
#from users.models import BookUser
#admin.site.register(BookUser)


# Import the UserProfile model individually.
from users.models import UserProfile

# Import the UserProfile model with Category and Page.
# If you choose this option, you'll want to modify the import statement you've already got to include UserProfile.
##from users.models import Category, Page, UserProfile
from users.models import UserProfile

admin.site.register(UserProfile)
