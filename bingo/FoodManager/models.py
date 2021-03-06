from django.db import models

class FoodManager(models.Model):
	manager_id = models.CharField(max_length=32)
	password = models.CharField(max_length=256)

class FoodInfo(models.Model):
	food_name = models.CharField(max_length=30)
	def __str__(self):
		return self.id + '.' + self.food_name
	def __unicode__(self):
		return u'%d. %s' % (self.id, self.food_name)
	rec_exp = models.IntegerField(default=1)
	icon_img_path1 = models.CharField(max_length=128)
	icon_img_path2 = models.CharField(max_length=128)
	frequency = models.IntegerField(default=0)

class FoodExtraInfo(models.Model):
	food_id = models.ForeignKey(FoodInfo)
	extra_info = models.TextField()
	etc = models.TextField()

class NoMixFoodInfo(models.Model):
	food_id1 = models.ForeignKey(FoodInfo, related_name="food1")
	food_id2 = models.ForeignKey(FoodInfo, related_name="food2")
	extra_info = models.TextField()

class ExtraFood(models.Model):
	food_name = models.CharField(max_length=30)
	frequency = models.IntegerField(default=0)

class FoodInfoHistory(models.Model):
	food = models.ForeignKey(FoodInfo)
	history_type = models.IntegerField(default=0)	# type 0: new data
													# type 1: modified data (except icon image)
													# type 2: modified data & icon

