from django.core.context_processors import request
from django.conf import settings


def variables(request):
	
	context_extras = {}
	
	context_extras['SETTINGS'] = settings
	
	return context_extras