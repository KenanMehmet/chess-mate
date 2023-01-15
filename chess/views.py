from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class ChessIndex(TemplateView):
    template_name = "chess/index.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
            {
                "title": "ChessMate"
            }
        )