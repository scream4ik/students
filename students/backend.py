from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.core.validators import email_re
 
class EmailBackend(ModelBackend):
    """
    Authenticates against django.contrib.auth.models.User.
    """
    def authenticate(self, username=None, password=None):
        #If username is an email address, then try to pull it up
        if email_re.search(username):
            try:
                user = User.objects.get(email=username, is_active=True)
            except User.DoesNotExist:
                return None
        else:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None
        if user.check_password(password):
            return user 
