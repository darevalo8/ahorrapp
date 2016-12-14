import random
from django.shortcuts import render
from django.views.generic import View
from users.viewmixins import LoginRequiredMixin


class Dashboard(LoginRequiredMixin, View):

    @staticmethod
    def get(request):
        frase = get_frase()
        return render(request, 'dashboard/dashboard.html', {'frase': frase})


def get_frase():
    numero = random.randrange(5)
    frases = {
        'frases': [
            {
                'texto': 'La gente de logros rara vez se sientan atras y dejan'
                         ' que pasen las cosas. '
                         'Salen y hacen que pasen las cosas.',
                'autor': 'Leonardo davinci.'
            },
            {
                'texto': 'Somos lo que pensamos. Todo lo que somos '
                         'surge con nuestros pensamientos. Con '
                         'nuestros pensamientos, hacemos nuestro mundo.',
                'autor': 'BUDA.'
            },
            {
                'texto': 'Para que los cambios sean autenticos, tienen '
                         'que ser dudaderos y consistentes. ',
                'autor': 'Anthony Robbins.'
            },

            {
                'texto': 'Es la mente la que hace el bien o el mal, '
                         'la que hace '
                         'desgraciado o feliz, '
                         'rico o pobre. ',
                'autor': 'Edmund Spencer.'
            },
            {
                'texto': 'Una de las grandes lecciones de la vida consiste '
                         'en aprender a comprender qué nos induce '
                         'a hacer lo que hacemos. ',
                'autor': 'Anthony Robbins.'
            }
        ]
    }
    context = frases['frases'][numero]
    return context
