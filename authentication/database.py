
from django.shortcuts import render
from .models import Link


def search_database(program,number):
	data = Link.objects.filter(program=program,number=number)
	return data


