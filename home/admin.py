from django.contrib import admin
from.models import Departments,Doctors,Booking,Contact

# Register your models here.
# this are use to register departments in admin part
admin.site.register(Departments)
admin.site.register(Contact)
admin.site.register(Doctors)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','patient_name','patient_phone','doctor_name','booking_date','booked_on')
admin.site.register(Booking,BookingAdmin)
