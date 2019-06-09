from django.shortcuts import render
from .models import User_Info,Sensor_Data,Doc,DocPatient,DocResquestNoti,Cont_Pulse,DocPatAck,EmergencyAct
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import sensorSerializer,userSerializer,AckSerializer,DocSerializer,contSerializer,EmergencyAck,DocListing,docReqPostSeriallizer,DocResquestSerializer,addPatientSerial
from django.views.decorators.csrf import csrf_exempt
from .forms import Auth,Date
import json
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import LineChart
import datetime


@api_view(['POST'])
def info(request):
    if request.method == 'POST':
        Userial = userSerializer(data = request.data)
        if Userial.is_valid():
            Userial.save()
            return Response(Userial.data,status=status.HTTP_201_CREATED)
        return Response(Userial.errors,status=status.HTTP_400_BAD_REQUEST)   
   

@api_view(['POST'])
def sensor(request):
    if request.method == 'POST':
        Sserial = sensorSerializer(data = request.data)
        if Sserial.is_valid():
            Sserial.save()
            return Response(Sserial.data,status=status.HTTP_201_CREATED)
        return Response(Sserial.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def docinfo(request):
    if request.method == 'POST':
        Dserial = DocSerializer(data = request.data)
        if Dserial.is_valid():
            Dserial.save()
            return Response(Dserial.data,status=status.HTTP_201_CREATED)
        return Response(Dserial.errors,status=status.HTTP_400_BAD_REQUEST)   
   

@api_view(['POST'])
def contpulse(request):
    if request.method == 'POST':
        Cserial = contSerializer(data = request.data)
        if Cserial.is_valid():
            Cserial.save()
            return Response(Cserial.data,status=status.HTTP_201_CREATED)
        return Response(Cserial.errors,status=status.HTTP_400_BAD_REQUEST)   

@api_view(['GET'])
def userdatadisplay(request):
    userdata = User_Info.object.all()
    sensordata = Sensor_Data.objects.all()
    return render(request,'displayuserdata.html',{'userdata':userdata,'sensordata':sensordata})

def auth(request):
    myusername = "not logged in"
    if request.method == "POST":
        form = Auth(request.POST)
        myusername = form['user'].value()
        mypassword = form['password'].value()
        if(verified(myusername,mypassword)):
            userdata = User_Info.objects.get(username = myusername)
            sensordata = Sensor_Data.objects.filter(user = myusername)
            Patient = DocPatient.objects.filter(Doctor = myusername)
            return render(request,'displayuserdata.html',{"username":myusername,"userdata" : userdata ,"sensordata":sensordata,"Patient":Patient})
        else:
            form = Auth()
    else:
        form = Auth()
    return render(request,'index.html',{'form':form})


def verified(myusername,mypassword):
    obj = User_Info.objects.get(username=myusername)
    if(obj.password == mypassword):
        return 1
    else:
        return 0

@api_view(['POST'])
def getDoc(request):
    if request.method == 'POST':
        snippets = Doc.objects.all()
        serializer = DocListing(snippets, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def DocPatReq(request):
    if request.method == 'POST':
        json_str=((request.body).decode('utf-8'))
        json_obj=json.loads(json_str)   
        obj = DocResquestNoti.objects.filter(destination = json_obj["destination"])
        serializer = DocResquestSerializer(obj,many = True)
        saver = serializer.data
        obj.delete()
        return Response(saver)

@api_view(['POST'])
def PostDocReq(request):
    if request.method == 'POST':
        json_str=((request.body).decode('utf-8'))
        json_obj=json.loads(json_str)   
        obj = docReqPostSeriallizer(data = request.data)
        check = DocResquestNoti.objects.filter(destination = json_obj["destination"],source = json_obj["source"])
        if not check:   
            if obj.is_valid():
                obj.save()
                return Response("Request Sent",status=status.HTTP_201_CREATED)
            return Response("Failed to send Request",status=status.HTTP_400_BAD_REQUEST)
        return Response("Request Already Sent. Please Wait for Reply")


@api_view(['POST'])
def savePatient(request):
    if request.method == 'POST':
        json_str=((request.body).decode('utf-8'))
        json_obj=json.loads(json_str)   
        obj = addPatientSerial(data = request.data)
        check = DocPatient.objects.filter(Doctor = json_obj["Doctor"],Patient = json_obj["Patient"])
        if not check:   
            if obj.is_valid():
                obj.save()
                return Response(" has been Added",status=status.HTTP_201_CREATED)
            return Response(" was Failed to Add",status=status.HTTP_400_BAD_REQUEST)
        return Response(" Already Exist")


@api_view(['POST'])
def ackpatsend(request):
    if request.method == 'POST':
        json_str=((request.body).decode('utf-8'))
        json_obj=json.loads(json_str)   
        obj = DocPatAck.objects.filter(Patient = json_obj["Patient"])
        serializer = AckSerializer(obj,many = True)
        saver = serializer.data
        obj.delete()
        return Response(saver)

@api_view(['POST'])
def patack(request):
    if request.method == 'POST':
        Userial = AckSerializer(data = request.data)
        if Userial.is_valid():
            Userial.save()
            return Response(Userial.data,status=status.HTTP_201_CREATED)
        return Response(Userial.errors,status=status.HTTP_400_BAD_REQUEST)   

""" def tempgraph(request,username):
            sensordata = Sensor_Data.objects.filter(user = username)
            result = []
            result.append(['time','pulse','temp'])
            for data in sensordata: 
                tmp = []
                t = (data.timestamp).time()
                mystr = " "
                mystr += str(t.hour)
                mystr += ":"
                mystr += str(t.minute)
                mystr += ":"
                mystr += str(t.second)
                tmp.append(mystr)
                tmp.append(data.pulse)
                tmp.append(data.temp)
                result.append(tmp)
            data_source = SimpleDataSource(data = result)
            chart = LineChart(data_source,html_id = 'plottemp_div',width=1500,height=1000)
            context = {'chart' : chart,'username' : username}
            return render(request, 'graph.html',context)
        
 """

def specgraph(request,username):
    if request.method == 'POST':
        form = Date(request.POST)
        indate = form['specdate'].value()
        indate = datetime.datetime.strptime(indate, '%Y-%m-%d').date()
        year = indate.year
        month = indate.month
        day = indate.day
        sensordata = Sensor_Data.objects.filter(user = username,timestamp__year = year , timestamp__month = month ,timestamp__day = day)
        Pulsedata = Cont_Pulse.objects.filter(user = username,timestamp__year = year , timestamp__month = month ,timestamp__day = day)
        result2 = []
        result2.append(['time','pulse'])
        result = []
        result.append(['time','pulse','temp'])
        for data in sensordata: 
            tmp = []
            t = (data.timestamp).time()
            mystr = " "
            mystr += str(t.hour)
            mystr += ":"
            mystr += str(t.minute)
            mystr += ":"
            mystr += str(t.second)
            tmp.append(mystr)
            tmp.append(data.pulse)
            tmp.append(data.temp)
            result.append(tmp)
            data_source = SimpleDataSource(data = result)
            chart = LineChart(data_source,html_id = 'first',width=1500,height=1000)
        for data1 in Pulsedata: 
            tmp = []
            t = (data1.timestamp).time()
            mystr = " "
            mystr += str(t.hour)
            mystr += ":"
            mystr += str(t.minute)
            mystr += ":"
            mystr += str(t.second)
            tmp.append(mystr)
            tmp.append(data1.pulsevalue)
            result2.append(tmp)
        data_source2 = SimpleDataSource(data = result2)
        chart2 = LineChart(data_source2,html_id = 'second',width=1500,height=1000)
        context = {'chart' : chart,'username' : username,'chart2':chart2}
        return render(request, 'graph.html',context)
    else:
            sensordata = Sensor_Data.objects.filter(user = username)
            Pulsedata = Cont_Pulse.objects.filter(user = username)
            result2 = []
            result2.append(['time','pulse'])
            result = []
            result.append(['time','pulse','temp'])
            for data in sensordata: 
                tmp = []
                t = (data.timestamp).time()
                mystr = " "
                mystr += str(t.hour)
                mystr += ":"
                mystr += str(t.minute)
                mystr += ":"
                mystr += str(t.second)
                tmp.append(mystr)
                tmp.append(data.pulse)
                tmp.append(data.temp)
                result.append(tmp)
            data_source = SimpleDataSource(data = result)
            chart = LineChart(data_source,html_id = 'first',width=1500,height=1000)
            for data1 in Pulsedata: 
                tmp = []
                t = (data1.timestamp).time()
                mystr = " "
                mystr += str(t.hour)
                mystr += ":"
                mystr += str(t.minute)
                mystr += ":"
                mystr += str(t.second)
                tmp.append(mystr)
                tmp.append(data1.pulsevalue)
                result2.append(tmp)
            data_source2 = SimpleDataSource(data = result2)
            chart2 = LineChart(data_source2,html_id = 'second',width=1500,height=1000)
            context = {'chart' : chart,'username' : username,'chart2':chart2}
            return render(request, 'graph.html',context)

@api_view(['POST'])
def emergencyadd(request):
    if request.method == 'POST':
        Userial = EmergencyAck(data = request.data)
        if Userial.is_valid():
            Userial.save()
            return Response(Userial.data,status=status.HTTP_201_CREATED)
        return Response(Userial.errors,status=status.HTTP_400_BAD_REQUEST)  

@api_view(['POST'])
def emergencysent(request):
    if request.method == 'POST':
        json_str=((request.body).decode('utf-8'))
        json_obj=json.loads(json_str)   
        obj = EmergencyAct.objects.filter(Doctor = json_obj["Doctor"])
        serializer = EmergencyAck(obj,many = True)
        saver = serializer.data
        obj.delete()
        return Response(saver)

@api_view(['POST'])
def getDoctors(request):
    if request.method == 'POST':
        json_str=((request.body).decode('utf-8'))
        json_obj=json.loads(json_str)   
        check = DocPatient.objects.filter(Patient = json_obj["Patient"])
        serializer = addPatientSerial(check,many = True)
        saver = serializer.data
        return Response(saver)