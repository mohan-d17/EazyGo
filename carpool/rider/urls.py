from django.urls import path 

from . import views

app_name = 'rider'

# urlpatterns = [
# 	path('' , views.index , name = "index"),
# 	url(r'^(?P<album_id>[0-9]+)/$' , views.detail , name = "detail"),
# 	url(r'^(?P<album_id>[0-9]+)/favorite/$' , views.favorite , name = "favorite")
# ]

# urlpatterns = [
# 	path('' , views.IndexView.as_view() , name = "index"),
# 	url(r'^(?P<pk>[0-9]+)/$' , views.DetailView.as_view() , name = "detail"),
# 	url(r'^album/add/$', views.createAlbum.as_view() , name = "album-add")
# ]

urlpatterns = [
	path('' , views.index , name = "ride"),
    path('drive_or_ride.html', views.drive_or_ride, name='drive_or_ride'),
    path('charts.html', views.charts, name='charts'),
    path('tables.html', views.charts, name='tables'),
	path('submit', views.rideInfo, name = "rideInfo"),
	path('processsing', views.statusUpdate, name = "statusUpdate"),
	path('success', views.rideSuccessful, name = "rideSuccessful"),
	# path('rideRemove', views.endRide, name = "endRide"),
]

