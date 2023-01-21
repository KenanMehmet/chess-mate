from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import PlayerSignupForm
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

class ChessPlayerSignup(TemplateView):
    template_name = "chess/signup.html"

    def get(self, request):
        form = PlayerSignupForm()
        return render(
            request, 
            self.template_name,
            {
                "title": "Sign up",
                "form": form
            }
        )

    def post(self, request):
        form = PlayerSignupForm(
            request.POST or None, 
            request.FILES
        )
        if form.is_valid():
            form.save()
            return redirect("dashboard")
        return render(
            request, 
            self.template_name,
            {
                "title": "Sign up",
                "form": form
            }
        )

class ChessPlayerDashboard(TemplateView):
    template_name = "chess/dashboard.html"

    def get(self, request):
        user = request.user
        return render(
            request, 
            self.template_name,
            {
                "title": "Dashboard",
                "user": user
            }
        )