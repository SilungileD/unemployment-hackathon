from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return render(request, 'accounts/home.html')

def profile(request):
	return render(request, 'accounts/profile.html')


def jobs(request):
	return render(request, 'accounts/available jobs.html')

def recruiter(request):
	return render(request, 'accounts/recruiter.html')

def aboutus(request):
	return render(request, 'accounts/aboutus.html')

def contactus(request):
	return render(request, 'accounts/contactus.html')


''' 
--accounts
---templates
-----accounts
--------dashbooard.html
--------profile.html
--------customer.html
'''