from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model


class EmailAuthBackend(object):

    def Emailauthenticate(self, username=None, password=None):

        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            user = get_user_model().objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, username):
        try:
            return get_user_model().objects.get(pk=username)
        except User.DoesNotExist:
            return None
