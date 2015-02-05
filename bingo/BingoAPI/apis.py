from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

import json

from FoodManager.models import *

def getFoodInfo(request):
	resp = {}
	try:
		foodInfoList = FoodInfo.objects.all().order_by('id')
		foodInfoList_json = []
		for foodInfo in foodInfoList:
			foodInfo_json = {}
			foodInfo_json['food_id'] = foodInfo.id
			foodInfo_json['food_name'] = foodInfo.food_name
			foodInfo_json['rec_exp'] = foodInfo.rec_exp_date
			icon1_temp = foodInfo.icon_img_path1
			temp = icon1_temp.split('/')
			icon1_temp = temp[len(temp)-1]
			foodInfo_json['icon1'] = 'http://http://www.thanksbingo.com/static/media/icons/' + icon1_temp
			icon2_temp = foodInfo.icon_img_path2
			temp = icon2_temp.split('/')
			icon2_temp = temp[len(temp)-1]
			foodInfo_json['icon2'] = 'http://http://www.thanksbingo.com/static/media/icons/' + icon2_temp
			foodInfo_json['frequency'] = foodInfo.frequency

			foodInfoList_json.append(foodInfo_json)
		resp['is_there_data'] = True
		resp['food_info_list'] = foodInfoList_json
	except ObjectDoesNotExist:
		resp['is_there_data'] = False

	return HttpResponse(json.dumps(resp))




# def updateFoodInfo(request, ?):
