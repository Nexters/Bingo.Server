from django.conf.urls import patterns, include, url
from FoodManager import views
from FoodManager import control

urlpatterns = patterns('',

	url(r'^$', views.index, name='index'),
	url(r'^login/', control.login, name='login'),
	url(r'^logout/', control.logout, name='logout'),
	url(r'^new_food/', views.newFood, name='new_food'),
	url(r'^reg_food/', control.regFood, name='reg_food'),
)