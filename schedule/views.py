from django.shortcuts import render

# Create your views here.


def schedule(request):
    """ A view to return the schedule page """

    return render(request, 'schedule/schedule.html')
