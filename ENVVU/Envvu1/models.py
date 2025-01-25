from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.views.generic import CreateView



class Blogcateg(models.Model):
	categ = models.CharField(max_length=100)
	def  __str__(self):
		return self.categ

class Career(models.Model):
	title = models.CharField(max_length=100)
	descrpt= models.TextField(max_length=100)
	qualif=models.CharField(max_length=100)
	exper= models.CharField(max_length=100)
	vac= models.IntegerField()
	def  __str__(self):
		return self.title


class Blog(models.Model):
	title = models.CharField(max_length=100)
	categ=models.ForeignKey(Blogcateg, on_delete=models.CASCADE, null=True, blank=True)
	content = models.TextField()
	date= models.DateTimeField(default=timezone.now)
	author=models.CharField(max_length=100)
	image= models.ImageField(default='default.jpg', upload_to='blog_pics')
	def  __str__(self):
		return self.title


class Gallery(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date= models.DateTimeField(default=timezone.now)
	image1= models.ImageField(default='default.jpg', upload_to='gallery')
	image2= models.ImageField(default='default.jpg', upload_to='gallery')
	image3= models.ImageField(default='default.jpg', upload_to='gallery')
	image4= models.ImageField(default='default.jpg', upload_to='gallery')
	image5= models.ImageField(default='default.jpg', upload_to='gallery')
	def  __str__(self):
		return self.title

class Applynow(models.Model):
	name = models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	yropas=models.IntegerField(null=True)
	qualification = models.CharField(max_length=100)
	jobtitle= models.CharField(max_length=100,null=True)
	experiance= models.IntegerField(null=True)
	cv= models.FileField(default='default.jpg', upload_to='CV')
	
	def  __str__(self):
		return self.name

