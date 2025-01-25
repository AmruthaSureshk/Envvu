from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('career/',views.career,name='career'),
    path('contact/',views.contact,name='contact'),
    path('digitalmarketing/',views.digitalmarketing,name='digitalmarketing'),
    path('faq/',views.faq,name='faq'),
    path('gallery/',views.gallery,name='gallery'),
    path('price/',views.price,name='price'),
    path('privacy/',views.privacy,name='privacy'),
    path('production/',views.production,name='production'),
    path('service/',views.service,name='service-details'),
    path('blog/<id>',views.blogdet,name='blogdet'),
    path('team/',views.team,name='team'),
    path('termsandconditions/',views.termsandconditions,name='termsandconditions'),
    path('webdevelopment/',views.webdevelopment,name='webdevelopment'),
    path('galldet/<id>',views.galldet,name='galldet'),
    path('applynow/',views.applynow,name='applynow'),
    path('contest/',views.contest,name='contest'),

]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)