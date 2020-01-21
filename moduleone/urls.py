from rest_framework.routers import SimpleRouter
from moduleone.views import *
simplert = SimpleRouter()

simplert.register('patients',PatientOps)
simplert.register('doctors',DoctorOps)
simplert.register('address',AddressOps)
simplert.register('hostpital',HospitalOps)
urlpatterns = simplert.urls
