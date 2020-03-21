from django.http import HttpResponse

def list(request, list_id): # pylint: disable=redefined-builtin
    return HttpResponse(content_type='application/json')
