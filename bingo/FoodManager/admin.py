from django.contrib import admin
from FoodManager.models import FoodManager, FoodInfo, FoodExtraInfo, NoMixFoodInfo, ExtraFoodList

class FoodManagerAdmin(admin.ModelAdmin):
	list_display = ('id', 'manager_id')

class FoodInfoAdmin(admin.ModelAdmin):
	list_display = ('id', 'food_name', 'rec_exp_date', 'icon_img_path1', 'icon_img_path2', 'frequency')

class FoodExtraInfoAdmin(admin.ModelAdmin):
	list_display = ('id', 'food_id', 'extra_info', 'etc')

class NoMixFoodInfoAdmin(admin.ModelAdmin):
	list_display = ('id', 'food_id1', 'food_id2', 'extra_info')

class ExtraFoodListAdmin(admin.ModelAdmin):
	list_display = ('id', 'food_name', 'frequency')

admin.site.register(FoodManager, FoodManagerAdmin)
admin.site.register(FoodInfo, FoodInfoAdmin)
admin.site.register(FoodExtraInfo, FoodExtraInfoAdmin)
admin.site.register(NoMixFoodInfo, NoMixFoodInfoAdmin)
admin.site.register(ExtraFoodList, ExtraFoodListAdmin)