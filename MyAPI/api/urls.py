from . import views
from django.conf.urls import url
from django.urls import path

app_name = 'api'

urlpatterns = [
	path("v1/developer/", views.developer),
	path("v1/organization/", views.organization)
]
