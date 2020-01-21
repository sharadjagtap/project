from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from moduleone.models import *


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorSerializer(ModelSerializer):
    #patients = PatientSerializer(many=True)
    class Meta:
        model = Doctor
        fields = '__all__'

class HospitalSerializer(ModelSerializer):
    #doctors = DoctorSerializer(many=True)
    class Meta:
        model = Hospital
        fields = '__all__'

class HospitalSerializer_dt(ModelSerializer):
    doctors = DoctorSerializer(many=True)
    class Meta:
        model = Hospital
        fields = '__all__'

class DoctorSerializer_pt(ModelSerializer):
    patients = PatientSerializer(many=True)
    class Meta:
        model = Doctor
        fields = '__all__'