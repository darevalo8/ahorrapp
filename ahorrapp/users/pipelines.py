def user_details(strategy, details, user=None, *args, **kwargs):
    """Update user details using data from provider."""
    if user and kwargs['is_new']:

        changed = False  # flag to track changes
        protected = ('username', 'id', 'pk', 'email') + \
            tuple(strategy.setting('PROTECTED_USER_FIELDS', []))
        # Update user model attributes with the new data sent by the current
        # provider. Update on some attributes is disabled by default, for
        # example username and id fields. It's also possible to disable update
        # on fields defined in SOCIAL_AUTH_PROTECTED_FIELDS.
        for name, value in details.items():
            if value and hasattr(user, name):
                # Check https://github.com/omab/python-social-auth/issues/671
                current_value = getattr(user, name, None)
                if not current_value or name not in protected:
                    changed |= current_value != value
                    setattr(user, name, value)

        if changed:
            strategy.storage.user.changed(user)
