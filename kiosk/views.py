from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import logout
from useradmin.models import *
from django.db.models import Avg,Q
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
import base64

def index(request):
    if request.session.get('user_id') is None:
        return JsonResponse({"kiosk":"session not found"})
    return JsonResponse({"kiosk":"app"})
        
@api_view(["POST"])
def login(request):
    data = JSONParser().parse(request)
    try:
        user=VendorLog.objects.get(Q(password=data['password'])&(Q(userName= data['username'])|Q(email= data['username'])))
        request.session['user_id'] = user.pk
        return Response({"msg":"user found","userid":user.pk})
    except VendorLog.DoesNotExist:
        return Response({"err":"user not found"})

def logout_view(request):
    id=request.session.get('user_id')
    if id:
        logout(request)
        return JsonResponse({"msg":'user logged out'})
    return JsonResponse({"msg":'not logged in '})
      