from rest_framework import serializers
from .models import User_Info,Sensor_Data,Cont_Pulse,Doc,DocPatient,DocResquestNoti,DocPatAck,EmergencyAct

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Info
        fields = '__all__'

class sensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor_Data
        fields = '__all__'

class contSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cont_Pulse
        fields = '__all__'

class DocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doc
        fields = '__all__'

class DocListing(serializers.ModelSerializer):
    city = serializers.CharField(source='user.city',read_only=True )
    email = serializers.CharField(source='user.email',read_only = True)
    class Meta:
        model = Doc
        fields = ('user','docid','city','email') 

        
class DocResquestSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source = 'source.city',read_only=True)
    email = serializers.CharField(source = 'source.email',read_only=True)
    name = serializers.CharField(source = 'source.name',read_only=True)
    dob = serializers.DateField(source = 'source.dob',read_only=True)
    gender = serializers.CharField(source = 'source.gender',read_only=True)
    bloodgrp = serializers.CharField(source = 'source.bloodgrp',read_only=True)
    age = serializers.CharField(source = 'source.age',read_only=True)

    class Meta:
        model = DocResquestNoti
        fields = ('source','destination','city','email','name','dob','gender','bloodgrp','age')

class docReqPostSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = DocResquestNoti
        fields = '__all__'

class addPatientSerial(serializers.ModelSerializer):
    class Meta:
        model = DocPatient
        fields = '__all__'

class AckSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocPatAck
        fields = '__all__'

class EmergencyAck(serializers.ModelSerializer):
    class Meta:
        model = EmergencyAct
        fields = '__all__'