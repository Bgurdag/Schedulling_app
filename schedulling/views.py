from django.shortcuts import render
from .models import Event
from .forms import ScheduleFrom
from django.http import HttpResponseRedirect

# Create your views here.
def homepage(request):
    events_list = Event.objects.all()

    context = {"events" :events_list}
    return render(request, "Official_calendar/index.html", context)
    return render(request, "Official_calendar/style.css", context)
    return render(request, "Official_calendar/launch.json", context)

def submit_event(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ScheduleFrom(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ScheduleFrom()

    return render(request, "schedulling/event.html", {"form": form})
