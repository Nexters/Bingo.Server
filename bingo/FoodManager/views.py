from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned

def index(request):
	if 'manager' in request.session:
		return redirect('/food_manager/new_food')

	return render(request, 'FoodManager/login.html')

def newFood(request):
	if not 'manager' in request.session:
		return redirect('/food_manager')

	return render(request, 'FoodManager/new_food_info.html')
