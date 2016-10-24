from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class UserProfile(User):
    avatar = models.URLField(default='', blank=True)
    slug = models.SlugField()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.username)
        super(UserProfile, self).save(force_insert, force_update, using,
                                      update_fields)

    @property
    def get_absolute_url(self):
        return reverse('auth_login')

    class Meta:
        app_label = 'users'
