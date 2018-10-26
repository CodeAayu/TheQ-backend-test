from django.contrib import admin
from django.urls import path
from testapp.views import savetheevent, showeventdetails, deleteevent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('neweventdetails/', savetheevent),
    path('showeventdetails/', showeventdetails),
    path('deleteevent/<int:id>', deleteevent),
]
