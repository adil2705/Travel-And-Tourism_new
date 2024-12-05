from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,FileResponse
from . forms import userdataForm,UserLoginForm,DemoDateForm
from .models import User,UserLogin,DemoDate,Buses,Flights
from django.db.models import Q
import numpy as np


def project(request):
	return render(request,"home.html")

def home(request):
	if 'email' not in request.session:
		return HttpResponse("<h1 align='center'>Session Expired</h1>")
	else:
		email=request.session['email']
		return render(request,'userhome.html',{'email':email})
 
def viewusers(request):
	users=User.objects.all()
	return render(request,'display.html',{'users':users})

def loginpage(request):
	form = UserLoginForm()
	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid():
			email=form.data["email"]
			password=form.data["password"]
			data=User.objects.filter(Q(email__iexact=email) & Q(password__iexact=password))
			if data:
				request.session['email']=email
				if 'email' not in request.session:
					return HttpResponse("Session Expired")
				else:
					return render(request,'userhome.html',{'email':email})
			else:
				return render(request,"login.html",{'form':form})
		else:
			form = UserLoginForm() 
	return render(request,'login.html',{'form':form})
def viewseats(request,travels):
	if 'email' not in request.session:
		return HttpResponse("<h1 align='center'>Session Expired</h1>")
	else:
		bus=Buses.objects.filter(Q(travels__iexact=travels))
		if bus:
			return render(request,'viewseats.html',{'bus':bus})
		else:
			return HttpResponse("not found")
		#return render(request,'viewseats.html',{'bus':bus})

def profile(request):
	if 'email' not in request.session:
		return HttpResponse("<h1 align='center'>Session Expired</h1>")
	else:
		email=request.session['email']
		user=User.objects.filter(Q(email__iexact=email))
		return render(request,'profile.html',{'user':user})

def busfilter(request):
	if request.method=="POST":
		dep=request.POST["dep"]
		arr=request.POST["arr"]
		d=request.POST["d"]
		buses=Buses.objects.filter(Q(departure_palce__iexact=dep) & Q(arrival_place__iexact=arr) & Q(date__iexact=d)) 
		return render(request,'busfilter.html',{'buses':buses})
		
def flightfilter(request):
	if request.method=="POST":
		dep=request.POST["dep"]
		arr=request.POST["arr"]
		d=request.POST["d"]
		flights=Flights.objects.filter(Q(departure_palce__iexact=dep) & Q(arrival_place__iexact=arr) & Q(date__iexact=d)) 
		return render(request,'bookflightpage.html',{'flights':flights})






def bpaymentpage(request,travels,id):
		if id==1:
			Buses.objects.filter(travels=travels).update(one="#1FACD4")
		elif id==2:
			Buses.objects.filter(travels=travels).update(two="#1FACD4")
		elif id==3:
			Buses.objects.filter(travels=travels).update(three="#1FACD4")
		elif id==4:
			Buses.objects.filter(travels=travels).update(four="#1FACD4")
		elif id==5:
			Buses.objects.filter(travels=travels).update(five="#1FACD4")
		elif id==6:
			Buses.objects.filter(travels=travels).update(six="#1FACD4")
		elif id==7:
			Buses.objects.filter(travels=travels).update(seven="#1FACD4")
		elif id==8:
			Buses.objects.filter(travels=travels).update(eight="#1FACD4")
		elif id==9:
			Buses.objects.filter(travels=travels).update(nine="#1FACD4")
		elif id==10:
			Buses.objects.filter(travels=travels).update(ten="#1FACD4")
		elif id==11:
			Buses.objects.filter(travels=travels).update(elven="#1FACD4")
		elif id==12:
			Buses.objects.filter(travels=travels).update(twelve="#1FACD4")
		elif id==13:
			Buses.objects.filter(travels=travels).update(thirtn="#1FACD4")
		elif id==14:
			Buses.objects.filter(travels=travels).update(fouthn="#1FACD4")
		elif id==15:
			Buses.objects.filter(travels=travels).update(fivethn="#1FACD4")
		elif id==16:
			Buses.objects.filter(travels=travels).update(sixthn="#1FACD4")
		email=request.session['email']
		request.session['travel']=travels
		buses=Buses.objects.filter(Q(travels__iexact=travels))
		return render(request,'buspaymentpage.html',{'buses':buses,'email':email,'id':id})

def forgotpassword(request):
	return render(request,'forgotpassword.html')

def confirmpayment(request):
	travels=request.session['travel']
	buses=Buses.objects.filter(Q(travels__iexact=travels))
	return render(request,'buscardpayment.html',{'v':buses,'travel':travels,})
	

def resetpassword(request):
	if request.method=="POST":
		email=request.POST["email"]
		opwd=request.POST["opwd"]
		npwd=request.POST["npwd"]
		r=User.objects.filter(Q(email__iexact=email) & Q(password__iexact=opwd)).update(password=npwd)
		if r:
			return render(request,'forgotpassword.html',{'msg':"password Udpated "})	
		else:
			return render(request,'forgotpassword.html',{'msg':"Password Not Udpated!"})
	else: 
		return HttpResponse("Not Successful")



def logout(request):
	del request.session['email']
	form = UserLoginForm()
	return render(request,'home.html')

def signuppage(request):
	form = userdataForm()
	if request.method == 'POST':
		form = userdataForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'signup.html',{'msg':"Account Created",'form':form,})
		else:
			form = userdataForm() 
	return render(request,'signup.html',{'form':form})



def booked(request):
	return render(request,'confirmpayment.html')


	
def tourconfirm(request):
	if 'email' not in request.session:
		return HttpResponse("<h1 align='center'>Session Expired</h1>")
	else:
		return render(request,'tourconfirm.html',)

def bookbuspage(request):
	if 'email' not in request.session:
		return HttpResponse("<h1 align='center'>Session Expired</h1>")
	else:
		buses=Buses.objects.all()
		return render(request,'bookbuspage.html',{'buses':buses})

def bookflightpage(request):
	if 'email' not in request.session:
		return HttpResponse("<h1 align='center'>Session Expired</h1>")
	else:
		flights=Flights.objects.all()
		return render(request,'bookflightpage.html',{'flights':flights})

def hospitalitypage(request):
	if 'email' not in request.session:
		return HttpResponse("<h1 align='center'>Session Expired</h1>")
	else:
		return render(request,'hospitalitypage.html')

def aboutuspage(request):
		return render(request,'aboutus.html')

def lr(request):
	return render(request,'linear_regression.html')

def demodate(request):
	form=DemoDateForm()
	return render(request,'demodatedisplay.html',{'form':form})

def flightticketdetails(request,flight):
	request.session['flight']=flight
	return render(request,'flightticket.html')


import logging
from django.http import HttpResponse
from django.shortcuts import render
from .models import Flights

# Configure logger
logger = logging.getLogger(__name__)

def flightpaymentpage(request):
    if 'email' not in request.session:
        return HttpResponse("<h1 align='center'>Session Expired</h1>")

    f = request.session.get('flight')
    if not f:
        logger.error("No flight session data found.")
        return HttpResponse("<h1 align='center'>Flight not found in session</h1>")

    try:
        flight = Flights.objects.filter(flight__iexact=f)
        if not flight.exists():
            logger.error(f"Flight with name {f} not found.")
            return HttpResponse("<h1 align='center'>Flight not found</h1>")

        fare = flight.first().fare
        return render(request, 'paymentpage.html', {'f': f, 'flight': flight, 'fare': fare})

    except Exception as e:
        logger.error(f"Error while fetching flight data: {e}")
        return HttpResponse("<h1 align='center'>An error occurred while processing the payment.</h1>")


    




def flightticketconfirm(request):
	f=request.POST['flight']
	c=request.POST['cl']
	n=request.POST['nt']
	fare=Flights.objects.filter(flight=f).values('fare')
	flight=Flights.objects.filter(Q(flight__iexact=f))
	email=request.session['email']
	return render(request,'flightticketconfirm.html',{'email':email,'fare':type(fare),})



import razorpay
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


# Initialize Razorpay client
client = razorpay.Client(auth=("rzp_test_7MmMzALQKLg4qp", "LvLLer1Qs7TY5Kovh555Pujp"))

@csrf_exempt
def create_order(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            amount = int(data.get("amount", 0))  # Amount from the template

            if amount <= 0:
                return JsonResponse({"error": "Invalid amount"}, status=400)

            order_data = {
                "amount": amount * 100,  # Convert to paise
                "currency": "INR",
                "receipt": "flight_receipt"
            }

            order = client.order.create(data=order_data)  # Create Razorpay order
            return JsonResponse({"order_id": order["id"], "key_id": "rzp_test_7MmMzALQKLg4qp"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

# View to handle successful payment

from django.http import HttpResponse

def payment_success(request):
    try:

	
        return render(request, "payment_success.html", )

    except Exception as e:
        print(f"Error in payment_success view: {str(e)}")
        return HttpResponse("Internal server error.", status=500)


# View to handle payment confirmation



# for bus
