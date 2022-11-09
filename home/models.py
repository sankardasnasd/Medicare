from django.db import models

# Create your models here.

class Departments(models.Model):
    department_name = models.CharField(max_length=200)
    department_description = models.TextField()

#  we want to see department name then use this code using a another string function
    def __str__(self):
        return self.department_name


class Doctors(models.Model):
    doctor_name = models.CharField(max_length=100)
    doctor_specialized = models.CharField(max_length=255)
    department_name = models.ForeignKey(Departments, on_delete = models.CASCADE)
    doctor_image = models.ImageField(upload_to='doctors')

    def __str__(self):
        return 'Dr-'+ self.doctor_name + '- (' + self.doctor_specialized +')'

class Booking(models.Model):
    patient_name = models.CharField(max_length = 250)
    patient_phone = models.CharField(max_length = 10)
    patient_email = models.EmailField()
    doctor_name = models.ForeignKey(Doctors,on_delete = models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now = True)


class Contact(models.Model):
    complainter_name = models.CharField(max_length=100)
    complainter_email = models.EmailField()
    complainter_subject = models.TextField()
    complianter_messege = models.CharField(max_length=1000)