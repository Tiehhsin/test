from django.http import HttpResponse
from django.test import TestCase

# Create your tests here.
def test(request):

    return HttpResponse("ok")

def test2(request):
    return HttpResponse("ok")