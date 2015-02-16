from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

import json

from FoodManager.models import *

def getFoodInfo(request):
	
	resp = {}
	
	try:
		food_info_list = FoodInfo.objects.all().order_by('id')
		food_info_list_json = []

		for food_info in food_info_list:
			food_info_json = {}
			food_info_json['food_id'] = food_info.id
			food_info_json['food_name'] = food_info.food_name
			food_info_json['rec_exp'] = food_info.rec_exp
			icon1_temp = food_info.icon_img_path1
			temp = icon1_temp.split('/')
			icon1_temp = temp[len(temp)-1]
			food_info_json['icon1'] = 'http://www.thanksbingo.com/static/media/icons/' + icon1_temp
			icon2_temp = food_info.icon_img_path2
			temp = icon2_temp.split('/')
			icon2_temp = temp[len(temp)-1]
			food_info_json['icon2'] = 'http://www.thanksbingo.com/static/media/icons/' + icon2_temp
			food_info_json['frequency'] = food_info.frequency

			food_info_list_json.append(food_info_json)

		resp['need_update'] = True
		resp['food_info_list'] = food_info_list_json
		resp['last_history'] = FoodInfoHistory.objects.all().order_by('id').last().id

	except ObjectDoesNotExist:
		resp['need_update'] = False

	return HttpResponse(json.dumps(resp))


def updateFoodInfo(request, last_history):
	
	resp = {}

	try:
		starting_his_id = int(last_history) + 1
		new_history_list = FoodInfoHistory.objects.filter(id__gte=starting_his_id)
		
		type0_list = [] # new data
		type1_list = [] # modified data (except icon image)
		type2_list = [] # modified data & icon
		
		for history in new_history_list:
			if history.history_type == 1:
				food_info = history.food
				data = {}
				data['food_id'] = food_info.id
				data['food_name'] = food_info.food_name
				data['rec_exp'] = food_info.rec_exp
				data['frequency'] = food_info.frequency

				type1_list.append(data)

			elif history.history_type == 0 or history.history_type == 2:
				food_info = history.food
				data = {}
				data['food_id'] = food_info.id
				data['food_name'] = food_info.food_name
				data['rec_exp'] = food_info.rec_exp
				icon1_temp = food_info.icon_img_path1
				temp = icon1_temp.split('/')
				icon1_temp = temp[len(temp)-1]
				data['icon1'] = 'http://www.thanksbingo.com/static/media/icons/' + icon1_temp
				icon2_temp = food_info.icon_img_path2
				temp = icon2_temp.split('/')
				icon2_temp = temp[len(temp)-1]
				data['icon2'] = 'http://www.thanksbingo.com/static/media/icons/' + icon2_temp
				data['frequency'] = food_info.frequency

				if history.history_type == 0:
					type0_list.append(data)
				elif history.history_type == 2:
					type2_list.append(data)
		# type 0: new data
		# type 1: modified data (except icon image)
		# type 2: modified data & icon
		resp['need_update'] = True
		resp['type0'] = type0_list
		resp['type1'] = type1_list
		resp['type2'] = type2_list
		resp['last_history'] = FoodInfoHistory.objects.all().order_by('id').last().id

	except ObjectDoesNotExist:
		resp['need_update'] = False

	return HttpResponse(json.dumps(resp))


def updateExtraFood(request):
	# class ExtraFoodList(models.Model):
	# 	food_name = models.CharField(max_length=30)
	# 	frequency = models.IntegerField(default=0)

	resp = {}

	if request.method == 'POST':
		food_name = request.POST.get('food_name')
		try:
			food = FoodInfo.objects.get(food_name=food_name)
			food.frequency = food.frequency + 1
			food.save()
			resp['result'] = True
			resp['message'] = 'Already existing food object in FoodInfo table.'
		except ObjectDoesNotExist:
			try:
				extra_food = ExtraFood.objects.get(food_name=food_name)
				extra_food.frequency = extra_food.frequency + 1
				extra_food.save()
				resp['result'] = True
				resp['message'] = 'Existing food object in ExtraFood table.'
			except objectDoesNotExist:
				extra_food = ExtraFood (
						food_name = food_name,
						frequency = 1
					)
				extra_food.save()
			except MultipleObjectsReturned:
				resp['result'] = False
				resp['message'] = 'MultipleObjectsReturned exception in ExtraFood.'
		except MultipleObjectsReturned:
			resp['result'] = False
			resp['message'] = 'MultipleObjectsReturned exception in FoodInfo.'

	else:
		resp['result'] = False
		resp['message'] = 'Wrong access'

	return HttpResponse(json.dumps(resp))

















