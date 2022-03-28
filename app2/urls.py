from django.urls import path
from app2.views import h3_sp
app_name='app2'
urlpatterns=[
    path('h3_sp/',h3_sp,name='h3_sp'),
]