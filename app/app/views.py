from django.shortcuts import redirect
from django.http import HttpRequest
import app.constants.template_constants as Templates
from django.contrib.auth import logout, authenticate, login
from app.helpers import authentication
from app.defined_api.datagen import Datagen
from app.defined_api.decision_tree import Tree

class TemplateView:
    """Built in Template Renderer View Level"""

    def __init__(self):
        pass

    def home(self, request):
        """Renders the home page."""

        TreeInstance = Tree()
        TreeInstance.decisionTree()
        
        assert isinstance(request, HttpRequest)

        if not request.user.is_authenticated:
            return redirect("login")

        return Templates.HOME.render_page(request)

    def datasets(self, request):
        """Renders the datasets page."""

        assert isinstance(request, HttpRequest)

        if not request.user.is_authenticated:
            return redirect("login")

        return Templates.DATASETS.render_page(request)

    def settings(self, request):
        """Renders the settings page."""

        assert isinstance(request, HttpRequest)

        if not request.user.is_authenticated:
            return redirect("login")

        return Templates.SETTINGS.render_page(request)

    def credibility(self, request):
        """Renders the credibility page."""

        assert isinstance(request, HttpRequest)

        if not request.user.is_authenticated:
            return redirect("login")

        return Templates.CREDIBILITY.render_page(request)

    def login(self, request):
        assert isinstance(request, HttpRequest)

        if request.user.is_authenticated == False:
            return Templates.LOGIN.render_page(request)
        return redirect("home")  # Change the home to your index page.

    def user_logout(self, request):
        logout(request)
        return redirect("login")
