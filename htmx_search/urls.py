from django.urls import path
from .views import search, index_1, index_2

urlpatterns = [
	path('home/', search, name='search'),
	path('search/', search, name='search'),
	path('index_2/', index_2, name='index_2'),
	path('', index_1, name='index_1'),

]