from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime,timedelta
from my_app.models import Timing
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
import xlwt
import xlrd
from django.http import HttpResponse

# Create your views here.
def main(request):
    return render(request, "main.html")

def about_us(request):
    return render(request, "about_us.html")

def contacts(request):
    return render(request, "contacts.html")

def Logout(request):
    Logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('main')

def Register(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        mobile=request.POST.get("mobile")
        password=request.POST.get("password")

        # If username already exists it will show error message
        if User.objects.filter(username=username):
            messages.error(request, "Username already exists! Please try another username")
            return redirect('Register')

        # create_user is inbuilt function to create a user
        myuser= User.objects.create_user(username=username,email=email,password=password)
        myuser.mobile=mobile

        myuser.save()
        messages.success(request, "User registered successfully...!\nWe have send you Email of successful registration...\nPlease Confirm")

        #Welcome Email...
        subject = "Welcome to Van Scheduler Registration!"
        message = "Hello " + myuser.username + "!\n" + "Welcome to Van Scheduler...!\nThank you for registering on Van Scheduler...!\nYour Username is "+myuser.username+"\n\n\nThanking You\nTeam Van Scheduler"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        try:
            send_mail(subject, message, from_email, to_list, fail_silently=True)

        except:
            print("Error sending email:")

        return redirect('Login')

    return render(request, "Register.html")


def services(request):
    return render(request, "services.html")


def Admin_Login(request):
    if request.method == 'POST':
        username = request.POST.get('adminusername')
        password = request.POST.get('adminpassword')

        # Validate the username and password
        if username == 'admin' and password == '123456789':
            # Redirect to the admin window
            messages.success(request, "Admin Login Successful..!")
            return redirect('Admin_window')
        else:
            # Display an error message or perform other actions
            messages.error(request, "Invalid admin credentials...!")
            return render(request, 'Admin_Login.html')
    return render(request, "Admin_Login.html")


def Admin_window(request):
    if request.method == 'POST' and 'download_excel' in request.POST:
        # Generate the Excel file
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="Todays_schedule.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Todays Schedule')

        # Sheet header
        row_num = 0
        columns = ['Fullname', 'Email', 'Mobile', 'Pickup Time', 'Droptime', 'College Name']

        for col_num, column_title in enumerate(columns):
            ws.write(row_num, col_num, column_title)

        # Sheet body
        rows = Timing.objects.all().values_list('fullname', 'email', 'mobile', 'pickuptime', 'droptime', 'college')

        for row_num, row in enumerate(rows, start=1):
            for col_num, cell_value in enumerate(row):
                ws.write(row_num, col_num, cell_value)

        wb.save(response)
        return response

    return render(request, "Admin_window.html")


# Login is required to access select_timing function
@login_required
def select_timing(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        pickuptime = request.POST.get('pickuptime')
        droptime = request.POST.get('droptime')
        college = request.POST.get('college')
        
        # if length of credentials is less than 3 then show error
        if len(fullname)<3 or len(email)<3 or len(mobile)<3 :
            messages.error(request,"Fill details properly!")

        # to set tomorrows date
        today_date=datetime.today()
        tomorrow_date=today_date+timedelta(1)

        # timings is an object created 
        timings = Timing(fullname=fullname, email=email, mobile=mobile, pickuptime=pickuptime, droptime=droptime, college=college, date=tomorrow_date)
        # print(fullname,email,mobile,pickuptime,droptime,college)
        timings.save()

        #Van schedule done Email...
        subject = "Your Van is Booked..!"
        message = "Hello " + timings.fullname + "!\n" + "Welcome to Van Scheduler...!\nYour Van on "+str(timings.date)+" is Booked..!\nYour Destiantion is "+timings.college+"\nYour pickup time is "+timings.pickuptime+" and drop time is "+timings.droptime+"\n\nWe wish you a very Happy and Safe Journey..!\n\n\nThanking You...!\nTeam Van Scheduler"
        from_email = settings.EMAIL_HOST_USER
        to_list = [timings.email]
        try:
            send_mail(subject, message, from_email, to_list, fail_silently=True)

        except :
            print("Error sending email:")

        # Data saving to Excel
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="Todays_schedule.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        # "Todays schedule" is Excel sheet name
        ws = wb.add_sheet('Todays Schedule')

        # Sheet header
        row_num = 0
        # These are the columns of Excel sheet
        columns = ['Fullname', 'Email', 'Mobile', 'Pickup Time', 'Droptime', 'College Name']

        for col_num, column_title in enumerate(columns):
            ws.write(row_num, col_num, column_title)

        # Sheet body
        rows = Timing.objects.all().values_list('fullname', 'email', 'mobile', 'pickuptime', 'droptime', 'college')

        for row_num, row in enumerate(rows, start=1):
            for col_num, cell_value in enumerate(row):
                ws.write(row_num, col_num, cell_value)

        wb.save(response)

        messages.success(request, "Your Van has been scheduled successfully..! We have send you an Email of Van-Booking....Plz Confirm...Thank you for using Van Scheduler..!")
        # return response
        return redirect('main')

    return render(request, "select_timing.html")


def Login(request):

    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        # authenticate is an inbuilt function which authenticates username and password
        user= authenticate(username=username, password=password)

        if user is not None:
            # login is inbuilt function
            login(request, user)
            messages.success(request, "Login Successful..!")
            return render(request, 'select_timing.html')
        
        else:
            messages.error(request, "Wrong Credentials..!")
            return redirect('Login')

    return render(request, "Login.html")

def loginex(request):
    return render(request, "loginex.html")


