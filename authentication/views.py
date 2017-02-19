from django.shortcuts import render
from .models import Link

from .example import *
from django.template import loader
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .database import *


@csrf_exempt
def information(request):
	if request.method == 'POST':
		result = {'response': 'success'}
		return JsonResponse(result,safe=False)

def main(request):
	if request.method=='GET':
		return render(request,'templates/index.html',{})

