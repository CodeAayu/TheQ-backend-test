from django.shortcuts import render
import datetime , json
from testapp.models import EventData
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse , JsonResponse

@csrf_exempt
def savetheevent(request):
    #print (request.body)
    data = json.loads(request.body)
    event_name = data["name"]
    event_date = datetime.datetime.strptime(data["date"],"%d%m%Y").date()
    event_description = data["description"]
    event_city = data["city"]
    EventData.objects.create(name=event_name, date=event_date, description=event_description, city=event_city)
    return HttpResponse("Event successfully saved!")

@csrf_exempt
def showeventdetails(request):
    if request.method == 'GET':
        data = EventData.objects.all().values()
        listing = list(data)
        #print (listing)
        return JsonResponse(listing, safe=False)
    return HttpResponse("Wrong request!")


def deleteevent(request):
    return HttpResponse("Event successfully saved!")
