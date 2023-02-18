from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('moses/',views.moses,name='moses'),
    path('termsandcondition/',views.termsandcondition,name='termsandcondition'),
    path('privacypolicy/',views.privacypolicy,name='privacypolicy'),
     path('test/',views.test,name='test')



]