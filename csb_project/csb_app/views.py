from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
from .models import timeSheetEntry
from .models import User

from dateutil.relativedelta import relativedelta
from dateutil import parser

@login_required
@csrf_exempt
def timesheet(request):

    sql = "SELECT * FROM csb_app_timesheetentry WHERE user_id = " + str(request.user.id)
    if request.GET.get('search'):
        sql += " AND comment LIKE '%" + request.GET.get('search') + "%'"
    print(sql)
    
    entries = timeSheetEntry.objects.raw(sql)
    return render(request, 'timesheet.html', {"entries": entries})

@login_required
def newpw(request):
    from django.contrib.auth.hashers import make_password
    
    if request.method == 'POST':
        
        password = request.POST.get('password')
        user = User.objects.get(username=request.user)
        user.set_password(password)
        user.save()
        return redirect('/')

    return render(request, 'newpw.html')

@login_required
@csrf_exempt
def newentry(request):
    if request.method == 'POST':
        user = request.user
        start = request.POST.get('start')
        end = request.POST.get('end')
        print(start)
        print(end)
        comment = request.POST.get('comment')
        time = relativedelta(parser.parse(end), parser.parse(start)).hours
        print(relativedelta(parser.parse(end), parser.parse(start)))
        completed = True #Only completed entries supported :S

        timeSheetEntry.objects.create(
                                    user=user,
                                    start=start,
                                    end=end,
                                    time=time,
                                    comment=comment,
                                    completed=completed)
        return redirect('/')

    return render(request, 'newentry.html')


