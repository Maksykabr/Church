from django.db import models

class days(models.Model):
	title = models.CharField(max_length=100, verbose_name = 'Назва дійства')
	content = models.TextField(blank=True, verbose_name = 'Особливості проведення')
	date_time = models.DateTimeField(verbose_name = 'Дата та час проведеня дійства')
	is_published = models.BooleanField(default = True, verbose_name = 'Упубліковано')
	day = models.ForeignKey('Category_days', on_delete=models.PROTECT, verbose_name = 'Категорія дня', null = True)


	def __str__(self):
		return self.title

class Category_days(models.Model):
	day_name = models.CharField(max_length=100, db_index=True)



	def __str__(self):
		return self.day_name






#розклад літургій:
#- id - int 
#-title - varchar - назва дня
#-content - text - назва дійства 
#-date_time - DataTime - дата дійства та час
#is_published - boolean - чи упубліковано