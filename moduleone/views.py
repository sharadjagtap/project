from moduleone.models import *
from moduleone.serializers import *
from rest_framework.viewsets import ModelViewSet

class DoctorOps(ModelViewSet):
    queryset = Doctor.activent.all()
    serializer_class = DoctorSerializer

class HospitalOps(ModelViewSet):
    queryset = Hospital.activent.all()
    serializer_class = HospitalSerializer

class PatientOps(ModelViewSet):
    queryset = Patient.activent.all()
    serializer_class = PatientSerializer

class AddressOps(ModelViewSet):
    queryset = Address.activent.all()
    serializer_class = AddressSerializer