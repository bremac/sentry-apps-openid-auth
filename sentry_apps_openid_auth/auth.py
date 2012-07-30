from django.contrib.auth.models import User
from openid.consumer.consumer import SUCCESS
 

class GoogleBackend(object):
    def authenticate(self, openid_response):
        if openid_response is None or openid_response.status != SUCCESS:
            return None

        def get_openid_attribute(attribute):
            return openid_response.getSigned(
                'http://openid.net/srv/ax/1.0',  attribute)

        email = get_openid_attribute('value.email')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = User.objects.create_user(email, email)
            user.first_name = get_openid_attribute('value.firstname')
            user.last_name = get_openid_attribute('value.lastname')
            user.save()

        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
