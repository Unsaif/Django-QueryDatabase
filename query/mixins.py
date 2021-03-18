from django.http import JsonResponse, HttpResponse
from django.db import connection
from .queryProcessing import qp


class AjaxFormMixin(object):
    def form_invalid(self, form):
        response = super(AjaxFormMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxFormMixin, self).form_valid(form)
        if self.request.is_ajax():
            
            query = form.cleaned_data['query']
            mycursor = connection.cursor()
        
            return qp(query, mycursor)