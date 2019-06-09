from django.urls import path,re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('post_user/', views.info),
    path('sensor_data/', views.sensor),
    path('docinfo/',views.docinfo),
    path('contdata/',views.contpulse),
    path('login/',views.auth),
    path('doclist/',views.getDoc),
    path('notify/',views.DocPatReq),
    path('docreq/',views.PostDocReq),
    path('addpatient/',views.savePatient),
    path('plot/<username>/',views.specgraph,name='plot'),
    path('ackpatsend/',views.ackpatsend),
    path('ack/',views.patack),
    path('getdoc/',views.getDoctors),
    path('emergencyack/',views.emergencyadd),
    path('mayday/',views.emergencysent),

]

urlpatterns = format_suffix_patterns(urlpatterns)