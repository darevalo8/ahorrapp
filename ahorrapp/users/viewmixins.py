from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):
    """
    minxins para que solo las personas logueadas accedas a un recursos
    se usa en las vistas basadas en clase
    """
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)
