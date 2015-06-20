from django.test import TestCase
from django.views.generic.base import TemplateView

# Create your views here.

class LandingView(TemplateView):
	template_name = 'base/index.html'



