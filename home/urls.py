
from django.urls import include, path 
from.import views

urlpatterns = [
    path('',views.homepage,name= 'homepage'),
    path('about',views.about,name= 'about'),
    path('booking',views.booking,name= 'booking'),
    path('doctors',views.doctors,name= 'doctors'),
    path('contact',views.contact,name= 'contact'),
    path('department',views.department,name= 'department'),
    # path('booking_messege',views.booking_messege,name = 'booking_messege')
    
  
]