from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse

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


def post(request):
	client = Clients()
	if request.method == "POST":
		client.first_name = request.POST.get('first_name', '')
		client.last_name = request.POST.get('last_name', '')
		client.email = request.POST.get('email', '')
		client.save()

	return render(request, 'post.html')