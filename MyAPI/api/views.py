from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from api.utils import rate_limit


@api_view(['GET','POST'])
@authentication_classes((SessionAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def developer(request):
	"""
	Set the default_limit for limiting the default users.
	Clients need to pass token in a header.
	"""
	default_limit = 5
	current_url = request.get_full_path()
	limit = default_limit

	if request.user and request.user.request_limits_developer != -1:
		limit = request.user.request_limits_developer

	if rate_limit(request.user.username, current_url, limit):
		content = {
			'status': 'request allowed'
		}
		# return Response(content, status=200)
	else:
		content = {
			'status': 'limit exceeded'
		}
		# return Response(content, status=429)
	return Response(content)


@api_view(['GET', 'POST'])
@authentication_classes((SessionAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def organization(request):
	"""
	Set the default_limit for limiting the default users.
	"""
	default_limit = 10
	limit = default_limit
	current_url = request.get_full_path()

	if request.user and request.user.request_limits_organization != -1:
		limit = request.user.request_limits_organization

	if rate_limit(request.user.username, current_url, limit):
		content = {
			'status': 'request allowed'
		}
	else:
		content = {
			'status': 'limit exceeded'
		}
	return Response(content)
