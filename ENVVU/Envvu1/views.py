from django.shortcuts import render,redirect
from . models import *
from django.core.mail import send_mail
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')
def blog(request):
	context= {
	'blog':Blog.objects.all(),
	'cat':Blogcateg.objects.all(),
	
	}
	return render(request,'blog.html',context)

def career(request):
	context= {
	'car':Career.objects.all(),
	
	}
	return render(request,'career.html',context)
def contact(request):
	return render(request,'contact.html')

def digitalmarketing(request):
	return render(request,'digitalmarketing.html')

def faq(request):
	return render(request,'faq.html')

def gallery(request):
	context= {
	'gall':Gallery.objects.all(),
	
	}
	return render(request,'gallery.html',context)

def price(request):
	return render(request,'price.html')

def privacy(request):
	return render(request,'privacy.html')
def production(request):
	return render(request,'production.html')

def service(request):
	return render(request,'service.html')

def blogdet(request, id):
	context ={
	'cat':Blogcateg.objects.all(),
	'blog2':Blog.objects.all().order_by('-date')[:3]
	
	} 
	context["data2"] = Blog.objects.get(id = id)

	return render(request,'single.html',context)
def team(request):
	return render(request,'team.html')

def termsandconditions(request):
	return render(request,'termsandconditions.html')

def webdevelopment(request):
	return render(request,'webdevelopment.html')


def galldet(request, id): 
    context ={} 
  
 
    context["data"] = Gallery.objects.get(id = id) 
          
    return render(request, "galldet.html", context) 




def applynow(request):
	if request.method=='POST' :
		if 'Appl' in request.POST :
			appl=Applynow()
			appl.name=request.POST['name']
			appl.email=request.POST['mail']
			appl.yropas=request.POST['yop']
			appl.jobtitle=request.POST['job']
			appl.qualification=request.POST['qualification']
			appl.experiance=request.POST['exp']
			appl.cv=request.FILES['cv']
			appl.save()
			return redirect('applynow')
	return render(request,'applynow.html')



def contest(request):
	if request.method=='POST':
		name=request.POST['name']
		email=request.POST['email']
		phone=request.POST['phone']
		place=request.POST['place']

		template = get_template('contest.txt')
		context = {'name' :name,'email' :email,'phone' :phone,'place' :place}
		content = template.render(context)
		email = EmailMessage(
                "Contest form Recieved",
                content,
                "Contest Form" + '',
                ['hashifmuhammed28@gmail.com'],
                headers = { 'Reply To': email }
            )
		email.send()
		messages.success(request, f'Your form is submitted , We will contact you soon')

	context= {

	}
	return render(request,'contest.html')