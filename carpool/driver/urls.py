from django.urls import path 

from . import views
from rider.models import ride
app_name = 'driver'


urlpatterns = [
    path('index.html', views.index, name='driverIndex'),
	path('driverHome.html' , views.driverHome , name = "driverHome"),
    path('drive_or_ride.html/', views.drive_or_ride, name='drive_or_ride'),
	path('driverInfo' , views.driverInfo , name = "driverInfo"),
	path('driveProcess' ,views.searchRider , name = "searchRider"),
	path('accept' ,views.acceptRider , name = "acceptRider" ),
	path('end', views.endRide , name ="endRide"),
]

