from django.views.generic import FormView
from django.http import HttpResponse
from .forms import JoinForm
from .mixins import AjaxFormMixin

# Create your views here.

class JoinFormView(AjaxFormMixin, FormView):
    form_class = JoinForm
    template_name  = 'home.html'
    success_url = '/form-success/'