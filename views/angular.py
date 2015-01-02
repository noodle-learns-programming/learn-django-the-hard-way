from django.http import HttpResponse

def add(req, n1, n2):
    content = 'Add: {0} + {1}'.format(n1, n2)
    return HttpResponse(content)