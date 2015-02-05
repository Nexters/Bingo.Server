from django.conf.urls import patterns, include, url
from BingoAPI import apis

urlpatterns = patterns('',

	url(r'^get_food_info/', apis.getFoodInfo, name='get_food_info'),
)