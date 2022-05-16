from django.shortcuts import render
from django.http import HttpResponse
#from .views import *

from .models import *

def index(request):
	monday = days.objects.filter(day_id = 1)
	tuesday = days.objects.filter(day_id = 2)
	wednesday = days.objects.filter(day_id = 3)
	thursday = days.objects.filter(day_id = 4)
	friday = days.objects.filter(day_id = 5)
	saturday = days.objects.filter(day_id = 6)
	sunday = days.objects.filter(day_id = 7)
	menu = ['Головна сторінка', 'про нас', 'і ще щось там']
	context = {
		'day_1' : 'Понеділок',
		'day_2' : 'Вівторок',
		'day_3' : 'Середа',
		'day_4' : 'Четверг',
		'day_5' : 'П\'ятниця',
		'day_6' : 'Субота',
		'day_7' : 'Неділя',
		'nazva' : 'Головна сторінка',
		'monday' : monday,
		'tuesday' : tuesday,
		'wednesday' : wednesday,
		'thursday' : thursday,
		'friday' : friday,
		'saturday' : saturday,
		'sunday' : sunday,
	}	
	return render(request, 'base.html', context = context,)
