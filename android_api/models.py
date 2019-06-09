from django.db import models
from datetime import date 


class User_Info(models.Model):
    username = models.CharField(primary_key=True, max_length=40) 
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True,max_length = 254) 
    name = models.CharField(max_length=50)  
    dob = models.DateField(max_length=8)
    age = models.IntegerField()    
    gender = models.CharField(max_length=6)
    bloodgrp = models.CharField(max_length=3)
    city = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)   #phone no valid field
    doctor = models.IntegerField()
    service = models.IntegerField()
   
    def __str__(self):
        return str(self.username)
    

class Sensor_Data(models.Model):
    user = models.ForeignKey(User_Info, on_delete = models.CASCADE)
    temp = models.FloatField()
    pulse = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return str(self.user)


   

class Cont_Pulse(models.Model):
    user = models.ForeignKey(User_Info,on_delete=models.CASCADE)
    pulsevalue = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True) 

    
    def __str__(self):
        return str(self.user)

   

class Doc(models.Model):
    user = models.ForeignKey(User_Info,on_delete = models.CASCADE)
    docid = models.CharField(max_length = 15)
    
    def __str__(self):
        return str(self.user)



class DocResquestNoti(models.Model):
    destination = models.ForeignKey(User_Info,on_delete= models.CASCADE,related_name= "DOCTOR")
    source = models.ForeignKey(User_Info,on_delete = models.CASCADE,related_name= "PATIENT")
    
    def __str__(self):
        return str(self.destination)


class DocPatient(models.Model):
    Doctor = models.ForeignKey(User_Info,on_delete=models.CASCADE)
    Patient = models.ForeignKey(User_Info,on_delete = models.CASCADE,related_name="soul")
 
    def __str__(self):
        return str(self.Patient)

class DocPatAck(models.Model):
    Doctor = models.ForeignKey(User_Info,on_delete=models.CASCADE)
    Patient = models.ForeignKey(User_Info,on_delete = models.CASCADE,related_name="space")
    

    def __str__(self):
        return str(self.Patient)


class EmergencyAct(models.Model):
   Doctor = models.ForeignKey(User_Info,on_delete=models.CASCADE)
   Patient = models.ForeignKey(User_Info,on_delete = models.CASCADE,related_name="time")
   
   def __str__(self):
        return str(self.Patient)





    