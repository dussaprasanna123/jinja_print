from django.urls import path
from app.views import *
app_name='something'
urlpatterns=[
    path('jinja_print/',jinja_print,name='jinja_print')
]