from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import get_object_or_404
from fake_api_gen.models import FakeApi
# Create your views here.


@csrf_protect
def apiview(request, api_slug):
	api_obj = get_object_or_404(FakeApi, slug=api_slug)

	if api_obj.req_auth and not request.user.is_authenticated:
		raise Http404

	if request.method != api_obj.request_method:
		return HttpResponseForbidden()

	if api_obj.response_body_type == 'JSON':
		content_type = 'application/json; charset=utf-8'
	elif api_obj.response_body_type == 'HTML':
		content_type = 'text/html; charset=utf-8'

	return HttpResponse(content=api_obj.response_body, content_type=content_type, status=api_obj.response_status_code)