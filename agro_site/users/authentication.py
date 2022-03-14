import email
# from django.contrib.auth.models import User
from .models import MyUser as User
from django.db.models import Q
from django.contrib.auth.hashers import check_password


class EmailAuthBackend(object):
    """
    Authenticate using e-mail account.
    """
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(Q(username__iexact=username) | Q(email__iexact=username) | Q(phone__iexact=username))
            if check_password(password, user.password):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
