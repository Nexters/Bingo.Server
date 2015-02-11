from django.conf.urls import patterns, include, url
from BingoAPI import apis

urlpatterns = patterns('',

	url(r'^get_food_info/', apis.getFoodInfo, name='get_food_info'),
	url(r'^update_food_info/(?P<last_history>\d+)/$', apis.updateFoodInfo, name='update_food_info'),
)