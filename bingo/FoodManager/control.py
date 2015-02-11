from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned

import os
import json

from FoodManager.models import *

from FoodManager.sessions import *
from FileUploader import FileUploader

def login(request):
	if request.method == 'POST':
		manager_id = request.POST.get('manager_id')
		password = request.POST.get('password')

		try:
			f_manager = FoodManager.objects.get(manager_id=manager_id, password=password)
		except ObjectDoesNotExist:
			return redirect('/food_manager')
		except MultipleObjectsReturned:
			return redirect('/food_manager')

		makeSessions(request, f_manager)

		return redirect('/food_manager/new_food')

	return redirect('/food_manager')

def logout(request):
	clearSessions(request)
	return redirect('/food_manager')

def regFood(request):
	if not 'manager' in request.session:
		return redirect('/food_manager')

	if request.method == 'POST':
		food_name = request.POST.get('food_name')
		food_icon1 = request.FILES['food_icon1']
		food_icon2 = request.FILES['food_icon2']
		food_rec_exp = request.POST.get('food_rec_exp')
		food_extra_info = request.POST.get('food_extra_info')

		# process of uploading food-icon-1 file
		icon1_uploader = FileUploader(food_icon1, 'media/icons/')
		food_icon1_fp = icon1_uploader.getFilePath()
		icon1_uploader.uploadFile()
		# process of uploading food-icon-1 file
		icon2_uploader = FileUploader(food_icon2, 'media/icons/')
		food_icon2_fp = icon2_uploader.getFilePath()
		icon2_uploader.uploadFile()

		food = FoodInfo (
				food_name = food_name,
				rec_exp = food_rec_exp,
				icon_img_path1 = food_icon1_fp,
				icon_img_path2 = food_icon2_fp,
				frequency = 1
			)
		food.save()

		FoodInfoHistory (
			food = food,
			history_type = 0
		).save()

		food_extra_info_list = _getFoodExtraInfoList(food_extra_info)
		for info in food_extra_info_list:
			if info=='' or info==' ' or info=='\n':
				continue
			FoodExtraInfo (
				food_id = food,
				extra_info = info,
				etc = ' '
			).save()

	return redirect('/food_manager')

def _getFoodExtraInfoList(food_extra_info):
	return food_extra_info.split('/')





