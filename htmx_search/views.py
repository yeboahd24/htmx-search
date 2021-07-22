from django.shortcuts import render
from django.db.models import Q
from django.views.generic.list import ListView

from .models import Clients

def search(request):

	query = request.GET.get("search", "")
	clients = ""
	if query:
		clients = Clients.objects.filter(
			Q(first_name__icontains=query)|Q(last_name__icontains=query)
			
			)
	else:
		clients = Clients.objects.all()[:5]

	return render(request, 'search.html', {"clients":clients})



def index_1(request):
	return render(request, 'index1.html')


def index_2(request):
	return render(request, 'index2.html')