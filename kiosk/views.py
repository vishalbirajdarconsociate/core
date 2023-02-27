from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from django.db.models import Avg,Q
from django.http import JsonResponse
# from .serializers import *
import base64

# Create your views here.
def index(request):
    return JsonResponse({"kiosk":"app"})