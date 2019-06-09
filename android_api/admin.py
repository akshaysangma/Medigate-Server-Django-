from django.contrib import admin
from .models import User_Info,Sensor_Data,Cont_Pulse,Doc,DocPatient,DocResquestNoti,DocPatAck,EmergencyAct

# Register your models here.
admin.site.register(User_Info)
admin.site.register(Sensor_Data)
admin.site.register(Cont_Pulse)
admin.site.register(Doc)
admin.site.register(DocPatient)
admin.site.register(DocResquestNoti)
admin.site.register(DocPatAck)
admin.site.register(EmergencyAct)