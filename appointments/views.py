from django.contrib import messages
from django.shortcuts import render
from users.forms import ManageHolidayForm
from django.http.response import HttpResponseForbidden
from .models import Appointment
from .models import WEEK_DAYS
from django.shortcuts import get_object_or_404, redirect, render
from users.decorators import allowed_users, user_not_confined
import datetime

# Create your views here.


def appointment(request):
    return render(request, 'appointments/reservation.html')

def my_appointments(request):
    return render(request, 'appointments/my-appointments.html')

@user_not_confined
def book_appointment(request):
    day = request.GET.get("day", None)
    time = request.GET.get("time", None)
    hour = time.split(":")[0]
    minute = time.split(":")[1]
    time = datetime.time(hour=int(hour), minute=int(minute))
    if Appointment.is_time_available(time, day):
        Appointment.objects.create(
            user = request.user,
            time = time,
            day = day,
        )
        messages.success(request, f"Appointment Booked Successfully For {time}.")
    else:
        messages.error(request, f"Appointment Already Booked.")
    return redirect('appointment')

def unbook_appointment(request):
    appointment_id = request.GET.get("ap_id", None)
    appointment = get_object_or_404(Appointment, id = appointment_id)
    if appointment.user == request.user:
        appointment.delete()
        messages.success(request, f"Appointment UnBooked Successfully.")
    else:
        return HttpResponseForbidden()
    return redirect('appointment')


