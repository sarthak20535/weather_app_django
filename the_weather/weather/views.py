import requests
from django.shortcuts import render,redirect
from .models import City
from .forms import CityForm

# Create your views here.

def index(request):
	
	url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=c46e77dfafcefae8916605a158e28773'
	# city='London'
	# app_id='c46e77dfafcefae8916605a158e28773'
    
	err_msg=''
	message = ''
	# CSS class
	message_class = ''
	if request.method == 'POST':
		form = CityForm(request.POST)

		if form.is_valid():
			new_city = form.cleaned_data['name']
			existing_city_count = City.objects.filter(name=new_city).count()
		
			if(existing_city_count==0):
				r=requests.get(url.format(new_city)).json()
				if(r['cod'] ==200):
					form.save()
				else:
					err_msg = 'City does not exist in the world!!'
			else:
				err_msg='City already exist in database!!'

		if err_msg:
			message  = err_msg
			message_class = 'is-danger'
		else:
			message = 'City added successfully'
			message_class = 'is-success'



		# instantiating city
	print(err_msg)
	form = CityForm()

	cities = City.objects.all()
# list weather_data contain dictionary for all cities
	weather_data = []

	for city in cities:

		r=requests.get(url.format(city)).json()
		# print(r.text)

	# As we want 4 things to show for a city so storing in a dict
		city_weather = {
	       'city' : city.name,
	       'temperature' : r['main']['temp'],
	       'description' : r['weather'][0]['description'] ,
	       'icon' :r['weather'][0]['icon'] ,


		    }
		weather_data.append(city_weather)


	context = {
			'weather_data':weather_data,
			'form' : form,
			'message' : message,
			'message_class' : message_class
			}

	return render(request,'weather/weather.html',context)

def delete_city(request,city_name):
	City.objects.get(name=city_name).delete()
	return redirect('home')