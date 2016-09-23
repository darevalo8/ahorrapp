from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class UserProfile(User):
    def get_absolute_url(self):
        return reverse('users:home')
