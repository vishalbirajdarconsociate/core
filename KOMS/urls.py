from django.urls import path, include
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('',chartApi),
    path('update/',updateOrderStatus),
    path('save/',saveOrder),
    path('search/',searchOrder),
    path('testjson/',testjson)
]