# home/views.py

from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self):
        context = super().get_context_data()
        return context