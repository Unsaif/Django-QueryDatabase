import logging
from django.http import JsonResponse, HttpResponse
from django.db import connection
from .queryProcessing import qp

logger = logging.getLogger(__name__)


class AjaxFormMixin(object):
    def _is_ajax(self, request):
        """
        Django 4+ removed HttpRequest.is_ajax, so rely on the header directly.
        """
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    def form_invalid(self, form):
        response = super(AjaxFormMixin, self).form_invalid(form)
        if self._is_ajax(self.request):
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxFormMixin, self).form_valid(form)
        if self._is_ajax(self.request):
            query = form.cleaned_data['query']
            mycursor = connection.cursor()
            try:
                return qp(query, mycursor)
            except Exception as exc:
                logger.exception("Query processing failed for '%s'", query)
                return JsonResponse(
                    {
                        'error': 'Server error while processing query: {}'.format(exc),
                        'query': query,
                    },
                    status=500,
                )
