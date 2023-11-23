from django.shortcuts import render
from .models import Event
from .forms import ScheduleFrom
from django.http import HttpResponseRedirect

# Create your views here.
def homepage(request):
    events_list = Event.objects.all()

    if request.method=="POST":
        form = ScheduleFrom(request.POST)
        eventN = request.POST["name"]
        sdtF= request.POST["sdt"]
        edtF = request.POST["edt"]
        # check whether it's valid:
        # if form.is_valid():
            # process the data in form.cleaned_data as required
        obj = Event(
            eventname = eventN, #form.cleaned_data["name"],
            start_date_time = sdtF, #form.cleaned_data["sdt"],
            end_date_time = edtF #form.cleaned_data["edt"]
        )
        obj.save()
        print("printed")
            # redirect to a new URL:
    else:
        form = ScheduleFrom()

    context = {"events" :events_list, "form":form}
    return render(request, "Official_calendar/index.html", context)

