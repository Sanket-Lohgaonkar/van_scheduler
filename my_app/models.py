from django.db import models

# Create your models here.
class register(models.Model):
    username= models.CharField(max_length=120)
    email= models.CharField(max_length=50)
    mobile= models.CharField(max_length=12)
    password= models.CharField(max_length=25)
    date=models.DateField()

    def __str__(self):
        return self.username
    
class Timing(models.Model):
    fullname=models.CharField(max_length=120)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=12)
    pickuptime=models.CharField(max_length=10)
    droptime=models.CharField(max_length=10)
    college=models.CharField(max_length=50)
    date=models.DateField()

    def __str__(self):
        return self.fullname

    
# class logins(models.Model):
#     username= models.CharField(max_length=120)
#     email= models.CharField(max_length=50)
#     password= models.CharField(max_length=25)

#     def __str__(self):
#         return self.username
    
# class select_timing(models.Model):
#     fullname=models.CharField(max_length=120)
#     email=models.CharField(max_length=50)
#     mobile=models.CharField(max_length=12)
#     pickuptime=models.CharField(max_length=10)
#     droptime=models.CharField(max_length=10)
#     college=models.CharField(max_length=50)
#     date=models.DateField()

#     def __str__(self):
#         return self.fullname
    

# class timings(models.Model):
    

#     fullname=models.CharField(max_length=120)
#     email=models.CharField(max_length=50)
#     mobile=models.CharField(max_length=12)
#     pickuptime = models.CharField(max_length=20)
#     droptime = models.CharField(max_length=20)
#     college = models.CharField(max_length=50)
#     date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.fullname